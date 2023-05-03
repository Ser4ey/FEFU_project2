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
                    'room_resident': '',
                    'reserve_user': '',
                }
                if self.is_admin:
                    room_data['room_resident'] = room_resident
                    room_data['reserve_user'] = reserve_user

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

            return json.dumps({
                'server_answer': 'Комната успешно зарезервирована/Комната уже занята',
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

            return json.dumps({
                'server_answer': 'Есть новые уведомления',
                'notifications': [
                    {
                        'notification_time': '21:43 09.03.2002',
                        'notification_title': 'Заголовок',
                        'notification_text': 'Текст уведомления',
                        'notification_read_status': True, # True - прочитано False - не прочитано
                    }
                ],
                'answer_status': 'ok'
            })
        # команды для админов
        elif command['command_name'] == 'get_all_users':
            # command = {
            #     'command_name': 'get_all_users',
            # }
            # все зарегестрированные пользователи

            return json.dumps({
                'server_answer': '',
                'users': [
                    {
                        'login': 'Jonh',
                        'password': '1234',
                        'is_admin': False,
                        'room_number': 5, # если нет комнаты то -1
                        'reserve_room_number': -1 # номер зарезервированной комнаты (-1 если нет)
                    },
                    {
                        'login': 'Jonh2',
                        'password': '12343',
                        'is_admin': True,
                        'room_number': -1,  # если нет комнаты то -1
                        'reserve_room_number': -1
                    }
                ],
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

            return json.dumps({
                'server_answer': 'Вы успешно заселили пользователя',
                'command_status': True, # команда успешно выполнена
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

    command4 = {"command_name": "get_rooms_list"}

    r4 = s.message_handle(json.dumps(command4))
    print(json.loads(r4))

