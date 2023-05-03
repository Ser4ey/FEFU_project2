import datetime
import sqlite3
import json
import data.config


class UsersDB:
    def __init__(self, path_to_db = data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_users()

    def create_table_of_users(self):
        sql = """
        create table IF NOT EXISTS `users` (
          `user_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
          `first_name` VARCHAR(255) not null,
          `last_name` VARCHAR(255) not null,
          `login` VARCHAR(255) not null,
          `password` VARCHAR(255) not null,
          'admin_status' BOOLEAN not null
        )"""
        self.execute(sql, commit=True)

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def user_register(self, login, password, first_name, last_name, admin_status=False):
        sql = "SELECT * FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)

        print(f"result = {result}\n")
        if result is None:
            sql_insert = "INSERT INTO users (login, password, first_name, last_name, admin_status) VALUES (?, ?, ?, ?, ?)"
            self.execute(sql_insert, (login, password, first_name, last_name, admin_status), commit=True)
            user_id = self.connection.cursor().lastrowid
            print("Вы успешно зарегистрировались")
            return True
        else:
            # print("Вы не смогли зарегистриророваться")
            return False

    def get_all_users(self):
        sql = "SELECT * FROM users"
        result = self.execute(sql, fetchall=True)
        return result

    def get_user_info(self, login):
        sql = "SELECT * FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)
        return result


class RoomsDB:
    def __init__(self, path_to_db = data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_rooms()

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_of_rooms(self):
        sql = """
        create table IF NOT EXISTS `rooms` (
          `room_floor` INT8 not null,
          `room_number` INT8 not null,
          `occupied` BOOLEAN null,
          `room_resident` varchar(255) not null,
          'reserve_list' VARCHAR[] not NULL,
          `room_id` INTEGER PRIMARY KEY AUTOINCREMENT not null
    )"""
        self.execute(sql, commit=True)

    def create_room(self, room_floor, room_number):
        pass

    def get_rooms_list(self):
        sql = "SELECT * FROM rooms"
        result = self.execute(sql, fetchall=True)
        rooms = []

        for item in result:
            rooms.append({
                'room_floor':item[0],
                'room_number':item[1],
                'occupied': bool(item[2]),
                'room_resident':item[3],
                'reserve_list': item[4]
            })

        rooms_list = []
        for floor in range(1, 4):
            for room_number in range(1, 6):
                room = next((r for r in rooms if r['room_floor'] == floor and r['room_number'] == room_number), None)
                if room:
                    rooms_list.append(room)
                else:
                    rooms_list.append({
                        'room_floor': floor,
                        'room_number': room_number,
                        'occupied': False,
                        'room_resident': '',
                        'reserve_list': []
                    })

        return json.dumps({
            'server_answer': 'Список комнат',
            'rooms': rooms_list,
            'answer_status': 'ok'
        })
            # return json.dumps({
            #     'server_answer':'Список комнат',
            #     'rooms': rooms
            # })


class NotificationDB:
    def __init__(self, path_to_db=data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_notification()

    def create_table_of_notification(self):
        sql = """
        create table IF NOT EXISTS `notification` (
        'login' VARCHAR(255) not null,
        'time' TIMESTAMP not null,
        'text' VARCHAR(255) not null,
        'read_status' BOOLEAN not null
        )"""
        self.execute(sql, commit=True)

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def add_notification(self, login, text):
        cur_datetime = datetime.datetime.now()
        insert = """INSERT INTO notification VALUES (?,?,?,?)"""
        self.execute(insert, (login, cur_datetime, text, False), commit=True)

    def get_notifications(self, login):
        sql = "SELECT * FROM notification WHERE login = ?"
        result = self.execute(sql, (login,), fetchall=True)
        if result is None:
            return []
        else:
            notification = []

            for item in result:
                notification.append({
                    'time': item[1],
                    'text': item[2],
                    'read_status': item[3],
                })
            sql_update = "UPDATE notification SET read_status = True WHERE login = ?"
            self.execute(sql_update, (login,), commit=True)

            return notification


if __name__ == '__main__':
    # db = UsersDB()
    # db.user_register("zxc2", "123", "Gleb", "Kim")
    # db.user_register("Stepik", "456", "Stepan", "Kot", admin_status=True)
    # # print(db.get_user_info("Sergey"))
    #
    # print(f"Список всех пользователей: {db.get_all_users()}")
    # {"command_name": "registe_r", "args": {"login":"zxc", "password":"123", "first_name":"gleb", "last_name":"kim"}}

    n = NotificationDB()
    # n.add_notification(444, 'refds')
    # n.add_notification(444, 'refds')
    # n.add_notification(444, 'refds')

    print(n.get_notifications(444))

