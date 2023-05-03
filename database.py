
import datetime
import sqlite3
import json
import data.config

# пример базы данных (его не объзательно использовать)
class Database:
    def __init__(self, path_to_db = data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_rooms()
        self.create_table_of_users()


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



    def user_login(self, login, password):
        sql = "SELECT * FROM users WHERE login = ? and password = ?"
        result = self.execute(sql, (login, password), fetchone=True)

        if result is not None:
            # sql_update = "UPDATE users SET login_status='active' WHERE user_id=?"
            # self.execute(sql_update, (result.user_id,), commit=True)
            print(f"Вы вошли в аккаунт")
            return True
        else:
            print(f"Вы не смогли войти в аккаунт, либо вы не зарегистрированы")
            return False

            # return json.dumps({
            #     'server_answer': f"Вы успешно вошли в аккаунт",
            #     'answer_status': 'ok'
            # })
        # else:
            # return json.dumps({
            #     'server_answer': f"Пользователя с такими данными не существует",
            #     'answer_status': 'ok'
            # })


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
            return False

    def login_status(self, login):
        sql = "SELECT login FROM users"
        result = self.execute(sql, (login,), fetchone=True)
        if result is not None:
            return True
        else:
            return False

    def get_admin_status(self, login):
        sql = "SELECT admin_status FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)
        if result is not None:
            admin_status = result[0]
            return admin_status
        else:
            return False

    def get_all_users(self):
        sql = "SELECT * FROM users"
        result = self.execute(sql, fetchall=True)

        users = []

        # for item in result:
        #     users.append({
        #         'user_id': item[0],
        #         'first_name': item[1],
        #         'last_name': item[2],
        #         # 'room_resident': item[3],
        #         'login': item[3],
        #         'password': item[4],
        #         'admin_status': bool(item[5])
        #     })

        return result



class UsrersDB:
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

    def __init__(self, path_to_db = data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_users()

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

        users = []
        # for item in result:
        #     users.append({
        #         'user_id': item[0],
        #         'first_name': item[1],
        #         'last_name': item[2],
        #         # 'room_resident': item[3],
        #         'login': item[3],
        #         'password': item[4],
        #         'admin_status': bool(item[5])
        #     })

        return result

    def get_user_info(self, login):
        sql = "SELECT * FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)
        return result
        # if result is not None:
        #     # status = result[0]
        #     print("Вы уже есть в системе")
        #     return
        # else:
        #     print("Вас нет в системе")
        #     return False

class RoomsDb:
    def __init__(self, path_to_db = data.config.path_to_database):
        self.path_to_db = path_to_db
        self.create_table_of_rooms()

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


if __name__ == '__main__':
    db = UsrersDB()
    db.user_register("zxc2", "123", "Gleb", "Kim")
    print(db.get_user_info("zxc"))
    # print(db.get_user_info("zxc2"))

    admin = UsrersDB()
    admin.user_register("Stepik", "456", "Stepan", "Kot", admin_status=True)
    # print(db.get_user_info("Sergey"))

    print(f"Список всех пользователей: {db.get_all_users()}")
    # {"command_name": "registe_r", "args": {"login":"zxc", "password":"123", "first_name":"gleb", "last_name":"kim"}}