import json
from database import UsersDB, RoomsDB, NotificationDB
# оброботавыет запросы, полученные сервером от клиента, и возвращает ответ на них, который сервер отправит клиенту
# + вносит соответсвующие изменения в базы данных и т.д


class ClientSession:
    def __init__(self):
        self.client_username = None
        self.client_password = None
        self.is_admin = False
        self.users_db = UsersDB()
        self.rooms_db = RoomsDB()
        self.notification_db = NotificationDB()

    def message_handle(self, command: str):
        try:
            command = json.loads(command)
            if not ('command_name' in command):
                return json.dumps({
                    'server_answer': 'no command_name in command',
                    'answer_status': 'problem'  # статус problem - только в случае неверного формата команды
                })
        except Exception as er:
            return json.dumps({
                'server_answer': 'invalid json',
                'answer_status': 'problem' # статус problem - только в случае неверного формата команды
            })
        if command["command_name"] == "login":
            user = self.users_db.get_user_info(command["args"]["login"])
            if user is None:
                return json.dumps({
                    'server_answer': 'Пользователя с такими данными не существует',
                    'login_status': False,
                    'answer_status': 'ok'
                })
            if str(user[4]) != str(command["args"]["password"]):
                return json.dumps({
                    'server_answer': 'Неверный пароль',
                    'login_status': False,
                    'answer_status': 'ok'
                })

            self.client_username = command["args"]["login"]
            self.client_password = command["args"]["password"]

            return json.dumps({
                'server_answer': 'Вы успешно вошли в аккаунт',
                'login_status': True,
                'answer_status': 'ok'
            })
        elif command['command_name'] == 'register':
            if command['args']['login'].strip() == '' or command['args']['password'].strip()=='':
                return json.dumps({
                    'server_answer': 'Имя пользователя или пароль не может быть пустым.',
                    'register_success_status': False,
                    'answer_status': 'ok'
                })

            user = self.users_db.get_user_info(command["args"]["login"])
            if user is not None:
                return json.dumps({
                    'server_answer': 'Пользователь с таким именем уже существует',
                    'register_success_status': False,
                    'answer_status': 'ok'
                })

            self.client_username = command['args']['login']
            self.client_password = command['args']['password']
            self.users_db.user_register(command["args"]["login"], command["args"]["password"], command["args"]["first_name"], command["args"]["last_name"], False)

            return json.dumps({
                'server_answer': 'Вы успешно зарегистрировались',
                'register_success_status': True,
                'answer_status': 'ok'
            })
        # команды для пользователей, которые вошли в аккаунт (мы уже знаем их логины, поэтому пользователю не нужно их передавать)
        elif command['command_name'] == 'admin_status':
            user = self.users_db.get_user_info(self.client_username)
            if user is None:
                return json.dumps({
                    'server_answer': '',
                    'is_admin': False,
                    'answer_status': 'ok'
                })
            if user[5]:
                self.is_admin = True
            return json.dumps({
                'server_answer': '',
                'is_admin': user[5],
                'answer_status': 'ok'
            })
        elif command['command_name'] == 'get_rooms_list':
            rooms_to_return = []
            for room in self.rooms_db.get_rooms_list():
                room_id, room_floor, room_number, occupied, room_resident, reserve_user = room

                room_data = {
                    'room_number': room_number,  # уникален для каждой комнаты
                    'room_floor': room_floor,
                    'occupied': occupied,  # True - комната занята False - комната свободна
                    'room_resident': room_resident,
                    'reserve_user': reserve_user
                }
                rooms_to_return.append(room_data)

            return json.dumps({
                    'server_answer': 'Список комнат',
                    'rooms': rooms_to_return,
                    'answer_status': 'ok'
                    }
                )
        elif command['command_name'] == 'reserve_room':
            # command = {
            #     'command_name': 'reserve_room',
            #     'args': {
            #         'room_floor': 1,
            #         'room_number': 1
            #     }
            # }

            # резервирование свободной комнаты, можно зарезервировать только 1 не занятую комнату
            # создаёт уведомление для пользователя
            # если админ подтверждает резервирование, то пользователь засиляется в комнату
            # print(f'AA: {self.rooms_db.select_one_room(reserve_user=self.client_username)}')
            if not (self.rooms_db.select_one_room(reserve_user=self.client_username) is None):
                self.notification_db.add_notification(self.client_username, 'У вас уже есть зарезервированная комната!',
                                                      'Невозможно зарезервировать комнату!')
                return json.dumps({
                    'server_answer': 'У вас уже есть зарезервированная комната!',
                    'reserve_status': 'not_ok',
                    'answer_status': 'ok'
                })
            current_room = self.rooms_db.select_one_room(room_floor=command['args']['room_floor'],
                                                         room_number=command['args']['room_number'])
            if current_room[3] or current_room[5] != '':
                self.notification_db.add_notification(self.client_username,
                                f"Комната {command['args']['room_floor']}:{command['args']['room_number']} - занята",
                                f'Невозможно зарезервировать комнату!')
                return json.dumps({
                    'server_answer': 'Комната уже занята(зарезервирована)',
                    'reserve_status': 'not_ok',
                    'answer_status': 'ok'
                })

            self.rooms_db.update_room_info(room_floor=command['args']['room_floor'],
                                           room_number=command['args']['room_number'],
                                           thing_to_change='reserve_user',
                                           new_data=self.client_username)
            self.notification_db.add_notification(self.client_username,
                 f"Комната {command['args']['room_floor']}:{command['args']['room_number']} - успешно зарезервирована!",
                 f'Комната зарезервирована!')

            return json.dumps({
                'server_answer': 'Комната успешно зарезервирована',
                'reserve_status': 'ok',
                'answer_status': 'ok'
            })
        elif command['command_name'] == 'get_notifications':
            # command = {
            #     'command_name': 'get_notifications',
            # }
            # Некоторые действия создают уведомления
            # получаем все уведомление
            # типы уведомлений:
            # 1) Комната успешно зарезервирована
            # 2) Админ не подтвердил вашу резервацую
            # 3) Вы заселены (Админ подтвердил вашу резервацую)
            # 4) Вы выселены
            notifications_to_return = []
            notifications = self.notification_db.get_notifications(self.client_username)
            if notifications:
                for i in notifications:
                    notifications_to_return.append({
                            'notification_time': i['time'],
                            'notification_title': i['title'],
                            'notification_text': i['text'],
                            'notification_read_status': i['read_status'],
                        }
                    )
            return json.dumps({
                'server_answer': 'Уведомления',
                'notifications': notifications_to_return[::-1],
                'answer_status': 'ok'
            })
        # команды для админов
        elif command['command_name'] == 'get_all_users':
            # command = {
            #     'command_name': 'get_all_users',
            # }
            # все зарегестрированные пользователи
            user_to_return = []
            for user in self.users_db.get_all_users():
                user_data = {
                        'login': user[3],
                        'password': user[4],
                        'is_admin': user[5],
                        'room_number': -1,
                        'reserve_room_number': -1
                    }
                user_room = self.rooms_db.select_one_room(room_resident=user[3])
                if user_room:
                    user_data['room_number'] = user_room[0]
                user_reserve_room = self.rooms_db.select_one_room(reserve_user=user[3])
                if user_reserve_room:
                    user_data['reserve_room_number'] = user_reserve_room[0]

                user_to_return.append(user_data)

            return json.dumps({
                'server_answer': '',
                'users': user_to_return,
                'answer_status': 'ok'
            })

        elif command['command_name'] == 'change_user_residence_status':
            # command = {
            #     'command_name': 'change_user_residence_status',
            #     'args': {
            #         'change_type': 'confirm_reserve/cansel_reserve/kick_from_room',
            #         'username': 'John', # мы и так знаем где John живёт или где хочет
            #         'reason': 'причина от админа, нужна для уведомления пользователю. '
            #                   'Например: Комитет по заселению одобрил вашу кандидатуру!'
            #     }
            # }

            # меняем статус проживание пользователя подтверждаем/отклоняем его бронь или выселяем пользователя
            # создаёт уведомление для пользователя
            if command['args']['change_type'] == 'confirm_reserve':
                user_room = self.rooms_db.select_one_room(reserve_user=command['args']['username'])
                print(user_room)
                if not user_room:
                    return json.dumps({
                        'server_answer': 'Пользователь нигде не заригистрирован',
                        'command_status': False,  # команда успешно выполнена
                        'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                        'answer_status': 'ok'
                    })
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'occupied', True)
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'room_resident', command['args']['username'])
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'reserve_user', '')

                self.notification_db.add_notification(command['args']['username'], 'Вы успешно засилены',
                                                      'Вы успешно засилены')
                return json.dumps({
                    'server_answer': 'Вы успешно заселили пользователя',
                    'command_status': True,  # команда успешно выполнена
                    'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                    'answer_status': 'ok'
                })

            if command['args']['change_type'] == 'cansel_reserve':
                user_room = self.rooms_db.select_one_room(reserve_user=command['args']['username'])
                if not user_room:
                    return json.dumps({
                        'server_answer': 'Пользователь нигде не заригистрирован',
                        'command_status': False,  # команда успешно выполнена
                        'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                        'answer_status': 'ok'
                    })
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'occupied', False)
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'room_resident', '')
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'reserve_user', '')

                self.notification_db.add_notification(command['args']['username'], 'Вам отказано в засилении!',
                                                      'Вам отказано в засилении!')
                return json.dumps({
                    'server_answer': 'Вы успешно отказали пользователю',
                    'command_status': True,  # команда успешно выполнена
                    'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                    'answer_status': 'ok'
                })

            if command['args']['change_type'] == 'kick_from_room':
                user_room = self.rooms_db.select_one_room(room_resident=command['args']['username'])
                if not user_room:
                    return json.dumps({
                        'server_answer': 'Пользователь нигде не живёт',
                        'command_status': False,  # команда успешно выполнена
                        'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                        'answer_status': 'ok'
                    })
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'occupied', False)
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'room_resident', '')
                self.rooms_db.update_room_info(user_room[1], user_room[2], 'reserve_user', '')

                self.notification_db.add_notification(command['args']['username'], 'Поздравляем! Вас выслели!',
                                                      'Поздравляем! Вас выслели!')
                return json.dumps({
                    'server_answer': 'Вы успешно выселели пользователя',
                    'command_status': True,  # команда успешно выполнена
                    'command_error': '',  # возможные ошибки, например нет пользователя. Тогда command_status==False
                    'answer_status': 'ok'
                })

            return json.dumps({
                'server_answer': f'Неизвестная команда:' + f"{command['args']['change_type']}",
                'command_status': False, # команда успешно выполнена
                'command_error': '', # возможные ошибки, например нет пользователя. Тогда command_status==False
                'answer_status': 'ok'
            })

        return json.dumps({
            'server_answer': f'unknown command: {command["command_name"]}',
            'answer_status': 'problem'
        })


if __name__ == '__main__':
    s = ClientSession()

    command2 = {
        'command_name': 'login',
        'args': {
            'login': 'Stepik',
            'password': 456
        }
    }
    # r1 = s.message_handle(json.dumps(command2))

    command3 = {
        'command_name': 'register',
        'args': {
            'login': 'Liza',
            'password': 123,
            'first_name': "Denis",
            'last_name': "Gusev",
        }
    }

    command4 = {
                'command_name': 'reserve_room',
                'args': {
                    'room_floor': 3,
                    'room_number': 3
                }
            }
    s.client_username='21'
    s.client_password='21'

    command5 = {
        'command_name': 'get_notifications'
    }

    command6 = {
        'command_name': 'change_user_residence_status',
        'args': {
            'change_type': 'confirm_reserve',
            'username': '21', # мы и так знаем где John живёт или где хочет
            'reason': 'причина от админа, нужна для уведомления пользователю. Например: Комитет по заселению одобрил вашу кандидатуру!'
        }
    }
    r4 = s.message_handle(json.dumps(command4))
    r4 = s.message_handle(json.dumps(command6))
    print(json.loads(r4))

