import keyboard
keyboard.unhook_all()
import os
import datetime
import sqlite3
import json
#import data.config
#from server_api import ClientSession
def read_key():
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            return event.name
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

class Draw:
    def StartMenu(self, choice):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 29) or (i == 20 and j == 29):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 69) or (i == 20 and j == 69):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 15 and j == 29) or (i == 25 and j == 29):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 15 and j == 69) or (i == 25 and j == 69):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')

                elif (i == 10 or i == 15) and (29 < j < 69):  # горизонталь
                    if choice == 'login':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 29 or j == 69) and (10 < i < 15):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 40):  # текст вход
                    print("Нажмите, чтобы войти.", end='')
                    j += 20

                elif (i == 20 or i == 25) and (29 < j < 69):  # горизонталь
                    if choice == 'signup':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 29 or j == 69) and (20 < i < 25):  # вертикаль
                    print("\u2503", end='')
                elif (i == 22 and j == 33):  # текст registration
                    print("Нажмите, чтобы зарегистрироваться.", end='')
                    j += 33
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def LogIn(self):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 29):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 69):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 15 and j == 29):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 15 and j == 69):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 15) and (29 < j < 69):  # горизонталь
                    print("\u2501", end='')
                elif (j == 29 or j == 69) and (10 < i < 15):  # вертикаль
                    print("\u2503", end='')
                elif (i == 8 and j == 42):
                    print("Вход в аккаунт", end='')
                    j += 13
                elif (i == 12 and j == 36):  # текст вход
                    print("Введите свои данные внизу", end='')
                    j += 24
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def SignUp(self):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 29) :
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 69):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 15 and j == 29):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 15 and j == 69):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 15) and (29 < j < 69):  # горизонталь
                    print("\u2501", end='')
                elif (j == 29 or j == 69) and (10 < i < 15):  # вертикаль
                    print("\u2503", end='')
                elif (i == 8 and j == 35):
                    print("Регистрация нового аккаунта", end='')
                    j += 26
                elif (i == 12 and j == 36):  # текст вход
                    print("Введите свои данные внизу", end='')
                    j += 24
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def GuestMenu(self, choice, first_name):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 25) or (i == 18 and j == 25) or (i == 26 and j == 25) or (
                        i == 2 and j == 90):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 70) or (i == 18 and j == 70) or (
                        i == 26 and j == 70) or (i == 2 and j == 95):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 14 and j == 25) or (i == 22 and j == 25) or (
                        i == 30 and j == 25) or (i == 4 and j == 90):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 14 and j == 70) or (i == 22 and j == 70) or (
                        i == 30 and j == 70) or (i == 4 and j == 95):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 14) and (25 < j < 70):  # горизонталь
                    if choice == 'RoomsTable':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 25 or j == 70) and (10 < i < 14):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 30):  # окно 1
                    print("Просмотреть список комнат", end='')
                    j += 24
                elif (i == 6 and j == (100 - len(f"Здравствуйте, {first_name}!")) / 2):
                    print(f"Здравствуйте, {first_name}!", end='')
                    j += len(f"Здравствуйте, {first_name}!") - 1
                elif (i == 18 or i == 22) and (25 < j < 70):  # горизонталь
                    if choice == 'RoomBooking':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 25 or j == 70) and (18 < i < 22):  # вертикаль
                    print("\u2503", end='')
                elif (i == 20 and j == 30):  # окно 2
                    print("Зарезервировать комнату", end='')
                    j += 22
                elif (i == 26 or i == 30) and (25 < j < 70):  # горизонталь
                    if choice == 'GuestStatus':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 25 or j == 70) and (26 < i < 30):  # вертикаль
                    print("\u2503", end='')
                elif (i == 28 and j == 30):  # окно 1
                    print("Информация о статусе проживания", end='')
                    j += 30
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def AdminMenu(self, choice, first_name):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 25) or (i == 18 and j == 25) or (i == 2 and j == 90):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 70) or (i == 18 and j == 70) or (
                        i == 2 and j == 95):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 14 and j == 25) or (i == 22 and j == 25) or (i == 4 and j == 90):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 14 and j == 70) or (i == 22 and j == 70) or (i == 4 and j == 95):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 14) and (25 < j < 70):  # горизонталь
                    if choice == 'RoomsTable':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 25 or j == 70) and (10 < i < 14):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 30):  # окно 1
                    print("Просмотреть список комнат", end='')
                    j += 24
                elif (i == 6 and j == (100 - len(f"Здравствуйте, {first_name}!")) / 2):
                    print(f"Здравствуйте, {first_name}!", end='')
                    j += len(f"Здравствуйте, {first_name}!") - 1
                elif (i == 18 or i == 22) and (25 < j < 70):  # горизонталь
                    if choice == 'GuestsList':
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 25 or j == 70) and (18 < i < 22):  # вертикаль
                    print("\u2503", end='')
                elif (i == 20 and j == 30):  # окно 2
                    print("Посмотреть список пользователей", end='')
                    j += 30
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def RoomsTable(self, button_id_x, button_id_y):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 9 and j == 8) or (i == 2 and j == 90) or (i == 9 and j == 20) or (
                        i == 9 and j == 32) or (i == 9 and j == 44) or (i == 9 and j == 56) or (i == 16 and j == 8) or (
                        i == 16 and j == 20) or (i == 16 and j == 32) or (i == 16 and j == 44) or (
                        i == 16 and j == 56) or (i == 23 and j == 8) or (i == 23 and j == 20) or (
                        i == 23 and j == 32) or (i == 23 and j == 44) or (i == 23 and j == 56):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 9 and j == 14) or (i == 2 and j == 95) or (i == 9 and j == 26) or (
                        i == 9 and j == 38) or (i == 9 and j == 50) or (i == 9 and j == 62) or (
                        i == 16 and j == 14) or (i == 16 and j == 26) or (i == 16 and j == 38) or (
                        i == 16 and j == 50) or (i == 16 and j == 62) or (i == 23 and j == 14) or (
                        i == 23 and j == 26) or (i == 23 and j == 38) or (i == 23 and j == 50) or (i == 23 and j == 62):
                    print("\u2513", end='')  # правый угол
                elif (i == 39 and j == 0) or (i == 12 and j == 8) or (i == 4 and j == 90) or (i == 12 and j == 20) or (
                        i == 12 and j == 32) or (i == 12 and j == 44) or (i == 12 and j == 56) or (
                        i == 19 and j == 8) or (i == 19 and j == 20) or (i == 19 and j == 32) or (
                        i == 19 and j == 44) or (i == 19 and j == 56) or (i == 26 and j == 8) or (
                        i == 26 and j == 20) or (i == 26 and j == 32) or (i == 26 and j == 44) or (i == 26 and j == 56):
                    print("\u2517", end='')  # левый нижний
                elif (i == 39 and j == 99) or (i == 12 and j == 14) or (i == 4 and j == 95) or (
                        i == 12 and j == 26) or (i == 12 and j == 38) or (i == 12 and j == 50) or (
                        i == 12 and j == 62) or (i == 19 and j == 14) or (i == 19 and j == 26) or (
                        i == 19 and j == 38) or (i == 19 and j == 50) or (i == 19 and j == 62) or (
                        i == 26 and j == 14) or (i == 26 and j == 26) or (i == 26 and j == 38) or (
                        i == 26 and j == 50) or (i == 26 and j == 62):
                    print("\u251b", end='')  # правый нижний
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 5 and j == 35):
                    print("Просмотр списка комнат", end='')
                    j += 21
                elif (i == 7 and j == 10):
                    print("1 этаж", end='')
                    j += 5
                elif (i == 9 or i == 12) and (8 < j < 14):  # горизонталь
                    if button_id_x==1 and button_id_y==1:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 8 or j == 14) and (9 < i < 12):  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 and j == 11):
                    print("1", end='')
                elif (i == 9 or i == 12) and (20 < j < 26):  # горизонталь
                    if button_id_x == 1 and button_id_y == 2:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 20 or j == 26) and (9 < i < 12):  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 and j == 23):
                    print("2", end='')
                elif (i == 9 or i == 12) and (32 < j < 38):  # горизонталь
                    if button_id_x == 1 and button_id_y == 3:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 32 or j == 38) and (9 < i < 12):  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 and j == 35):
                    print("3", end='')
                elif (i == 9 or i == 12) and (44 < j < 50):  # горизонталь
                    if button_id_x == 1 and button_id_y == 4:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 44 or j == 50) and (9 < i < 12):  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 and j == 47):
                    print("4", end='')
                elif (i == 9 or i == 12) and (56 < j < 62):  # горизонталь
                    if button_id_x == 1 and button_id_y == 5:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 56 or j == 62) and (9 < i < 12):  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 and j == 59):
                    print("5", end='')
                elif (i == 14 and j == 10):
                    print("2 этаж", end='')
                    j += 5
                elif (i == 16 or i == 19) and (8 < j < 14):  # горизонталь
                    if button_id_x == 2 and button_id_y == 1:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 8 or j == 14) and (16 < i < 19):  # вертикаль
                    print("\u2503", end='')
                elif (i == 17 and j == 11):
                    print("1", end='')
                elif (i == 16 or i == 19) and (20 < j < 26):  # горизонталь
                    if button_id_x == 2 and button_id_y == 2:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 20 or j == 26) and (16 < i < 19):  # вертикаль
                    print("\u2503", end='')
                elif (i == 17 and j == 23):
                    print("2", end='')
                elif (i == 16 or i == 19) and (32 < j < 38):  # горизонталь
                    if button_id_x == 2 and button_id_y == 3:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 32 or j == 38) and (16 < i < 19):  # вертикаль
                    print("\u2503", end='')
                elif (i == 17 and j == 35):
                    print("3", end='')
                elif (i == 16 or i == 19) and (44 < j < 50):  # горизонталь
                    if button_id_x == 2 and button_id_y == 4:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 44 or j == 50) and (16 < i < 19):  # вертикаль
                    print("\u2503", end='')
                elif (i == 17 and j == 47):
                    print("4", end='')
                elif (i == 16 or i == 19) and (56 < j < 62):  # горизонталь
                    if button_id_x == 2 and button_id_y == 5:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 56 or j == 62) and (16 < i < 19):  # вертикаль
                    print("\u2503", end='')
                elif (i == 17 and j == 59):
                    print("5", end='')
                elif (i == 21 and j == 10):
                    print("3 этаж", end='')
                    j += 5
                elif (i == 23 or i == 26) and (8 < j < 14):  # горизонталь
                    if button_id_x == 3 and button_id_y == 1:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 8 or j == 14) and (23 < i < 26):  # вертикаль
                    print("\u2503", end='')
                elif (i == 24 and j == 11):
                    print("1", end='')
                elif (i == 23 or i == 26) and (20 < j < 26):  # горизонталь
                    if button_id_x == 3 and button_id_y == 2:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 20 or j == 26) and (23 < i < 26):  # вертикаль
                    print("\u2503", end='')
                elif (i == 24 and j == 23):
                    print("2", end='')
                elif (i == 23 or i == 26) and (32 < j < 38):  # горизонталь
                    if button_id_x == 3 and button_id_y == 3:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 32 or j == 38) and (23 < i < 26):  # вертикаль
                    print("\u2503", end='')
                elif (i == 24 and j == 35):
                    print("3", end='')
                elif (i == 23 or i == 26) and (44 < j < 50):  # горизонталь
                    if button_id_x == 3 and button_id_y == 4:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 44 or j == 50) and (23 < i < 26):  # вертикаль
                    print("\u2503", end='')
                elif (i == 24 and j == 47):
                    print("4", end='')
                elif (i == 23 or i == 26) and (56 < j < 62):  # горизонталь
                    if button_id_x == 3 and button_id_y == 5:
                        print("\u2584", end='')
                    else:
                        print("\u2501", end='')
                elif (j == 56 or j == 62) and (23 < i < 26):  # вертикаль
                    print("\u2503", end='')
                elif (i == 24 and j == 59):
                    print("5", end='')
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def RoomBooking(self):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 25) or (i == 18 and j == 25) or (i == 2 and j == 90):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 70) or (i == 18 and j == 70) or (
                        i == 2 and j == 95):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 14 and j == 25) or (i == 22 and j == 25) or (i == 4 and j == 90):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 14 and j == 70) or (i == 22 and j == 70) or (i == 4 and j == 95):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 14) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (10 < i < 14):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 30):  # окно 1
                    print("Этаж", end='')
                    j += 3
                elif (i == 6 and j == 40):
                    print("Зарезервировать комнату", end='')
                    j += 22
                elif (i == 18 or i == 22) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (18 < i < 22):  # вертикаль
                    print("\u2503", end='')
                elif (i == 20 and j == 30):  # окно 2
                    print("Номер", end='')
                    j += 4
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def GuestStatus(self):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 25) or (i == 18 and j == 25) or (i == 26 and j == 25) or (
                        i == 2 and j == 90):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 70) or (i == 18 and j == 70) or (
                        i == 26 and j == 70) or (i == 2 and j == 95):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 14 and j == 25) or (i == 22 and j == 25) or (
                        i == 30 and j == 25) or (i == 4 and j == 90):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 14 and j == 70) or (i == 22 and j == 70) or (
                        i == 30 and j == 70) or (i == 4 and j == 95):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 14) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (10 < i < 14):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 30):  # окно 1
                    print("Этаж", end='')
                    j += 3
                elif (i == 5 and j == 30):
                    print("Информация о вашем статусе проживания", end='')
                    j += 36
                elif (i == 18 or i == 22) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (18 < i < 22):  # вертикаль
                    print("\u2503", end='')
                elif (i == 20 and j == 30):  # окно 2
                    print("Номер", end='')
                    j += 4
                elif (i == 26 or i == 30) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (26 < i < 30):  # вертикаль
                    print("\u2503", end='')
                elif (i == 28 and j == 30):  # окно 3
                    print("Статус комнаты", end='')
                    j += 13
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def GuestsList(self):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 2 and j == 90):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 2 and j == 95):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 4 and j == 90):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 4 and j == 95):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 6 and j == 35):
                    print("Просмотр списка гостей", end='')
                    j += 21
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                elif (i == 10 and j == 5):
                    print("Хуила 1")
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def ManageBooking(self, login, floor, number, occupied, is_admin):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0) or (i == 10 and j == 25) or (i == 18 and j == 25) or (i == 26 and j == 25) or (
                        i == 2 and j == 90) or (i == 34 and j == 25):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99) or (i == 10 and j == 70) or (i == 18 and j == 70) or (
                        i == 26 and j == 70) or (i == 2 and j == 95) or (i == 34 and j == 70):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0) or (i == 14 and j == 25) or (i == 22 and j == 25) or (
                        i == 30 and j == 25) or (i == 4 and j == 90) or (i == 38 and j == 25):
                    print("\u2517", end='')
                elif (i == 39 and j == 99) or (i == 14 and j == 70) or (i == 22 and j == 70) or (
                        i == 30 and j == 70) or (i == 4 and j == 95) or (i == 38 and j == 70):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 10 or i == 14) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (10 < i < 14):  # вертикаль
                    print("\u2503", end='')
                elif (i == 12 and j == 30) and is_admin: # окно 1
                    print(f"Логин: {login}", end='')
                    j += len(f"Логин: {login}") - 1
                elif (i == 7 and j == 35):
                    print("Управление бронированием", end='')
                    j += 23
                elif (i == 18 or i == 22) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (18 < i < 22):  # вертикаль
                    print("\u2503", end='')
                elif (i == 20 and j == 30):  # окно 2
                    print(f"Этаж: {floor}", end='')
                    j += len(f"Этаж: {floor}") - 1
                elif (i == 26 or i == 30) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (26 < i < 30):  # вертикаль
                    print("\u2503", end='')
                elif (i == 28 and j == 30):  # окно 3
                    print(f"Этаж: {number}", end='')
                    j += len(f"Этаж: {number}") - 1
                elif (i == 34 or i == 38) and (25 < j < 70):  # горизонталь
                    print("\u2501", end='')
                elif (j == 25 or j == 70) and (34 < i < 38):  # вертикаль
                    print("\u2503", end='')
                elif (i == 36 and j == 30):  # окно 4
                    if occupied:
                        print("Занята", end='')
                        j += 5
                    else:
                        print("Свободна", end='')
                        j += 7
                elif (i == 2 or i == 4) and (90 < j < 95):  # горизонталь
                    print("\u2501", end='')
                elif (j == 90 or j == 95) and (2 < i < 4):  # вертикаль
                    print("\u2503", end='')
                elif (i == 3 and j == 92):  # уведомление
                    print("@", end='')
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1
    def Notifications(self, NotificationTitle, NotificationDate, Notification):
        clear_console()
        i = 0
        while i < 40:
            j = 0
            while j < 100:
                if (i == 0 and j == 0):
                    print("\u250f", end='')  # левый верхний угол
                elif (i == 0 and j == 99):  # правый угол
                    print("\u2513", end='')
                elif (i == 39 and j == 0):
                    print("\u2517", end='')
                elif (i == 39 and j == 99):
                    print("\u251b", end='')
                elif (i == 0 or i == 39):  # горизонталь
                    print("\u2501", end='')
                elif j == 0 or j == 99:  # вертикаль
                    print("\u2503", end='')
                elif (i == 6 and j == 40):
                    print("Просмотр уведомлений", end='')
                    j += 19
                elif (i == 9 and j == (100 - len(NotificationTitle) - len(NotificationDate) - 3) / 2):
                    print(f"{NotificationTitle} в {NotificationDate}", end='')
                    j += len(NotificationTitle) + len(NotificationDate) + 2
                elif (i == 10 and j == (100 - len(Notification)) / 2):
                    print(Notification, end='')
                    j += len(Notification) - 1
                else:
                    print(" ", end='')
                j = j + 1
            print()
            i = i + 1

Draw=Draw()
#ClientSession = ClientSession()

#СТАРТОВОЕ МЕНЮ
key='w'
choice = 'login'
while key != 'Esc':
    while key != 'enter':
        if key == 'w':
            choice = 'login'
        if key == 's':
            choice = 'signup'
        Draw.StartMenu(choice)
        key=read_key()
    input()
    login = 'unknown'
    password = 'unknown'
    first_name = 'unknown'
    last_name = 'unknown'
    is_admin = False
    #ВХОД
    if choice == 'login':
        #command = json.dumps({{"command_name": "login", "args": {{"login": f"{login}", "password": f"{password}"}}}})
        #while json.loads(ClientSession.message_handle(command))['login_status'] != True:
        key = 'w'
        while key != 'enter':
            Draw.LogIn()
            print("Введите логин: ", end="")
            login = input()
            print("Введите пароль: ", end="")
            password = input()
            key = read_key()
        #command = json.dumps({{"command_name": "login", "args": {{"login": f"{login}", "password": f"{password}"}}}})

    #РЕГИСТРАЦИЯ
    if choice == 'signup':
        #command = json.dumps({{"command_name": "register", "args": {{"login": f"{login}", "password": f"{password}", "first_name": f"{first_name}", "last_name": f"{last_name}"}}}})
        #while json.loads(ClientSession.message_handle(f'{{"command_name": "register", "args": {{"login": "{login}", "password": "{password}", "first_name": "{first_name}", "last_name": "{last_name}"}}}}'))['register_success_status'] != True:
        key = 'w'
        while key != 'enter':
            Draw.SignUp()
            print("Придумайте логин: ", end="")
            login = input()
            print("Придумайте пароль: ", end="")
            password = input()
            print("Ваше имя: ", end="")
            first_name = input()
            print("Ваша фамилия: ", end="")
            last_name = input()
            key = read_key()
         #command = json.dumps({{"command_name": "register", "args": {{"login": f"{login}", "password": f"{password}", "first_name": f"{first_name}", "last_name": f"{last_name}"}}}})
    #command = json.dumps({"command_name": "login_status"})
    #is_admin = json.loads(ClientSession.message_handle(command))['is_admin']
    is_admin = True

    if is_admin == True:
    # МЕНЮ АДМИНА
        key='w'
        choice = 'RoomsTable'
        while key != 'enter':
            if key == 'w':
                choice = 'RoomsTable'
            if key == 's':
                choice = 'GuestsList'
            if key == 'q':
                choice = 'Notifications'
            Draw.AdminMenu(choice, first_name)
            key=read_key()
        input()
    else:
    # МЕНЮ ГОСТЯ
        key='w'
        button_id=0
        choice = 'RoomsTable'
        while key != 'enter':
            if key == 's' and button_id < 2:
                button_id += 1
            elif key == 'w' and button_id > 0:
                button_id -= 1
            if key == 'q':
                choice = 'Notifications'
            if button_id == 0:
                choice = 'RoomsTable'
            elif button_id == 1:
                choice = 'RoomBooking'
            elif button_id == 2:
                choice = 'GuestStatus'
            Draw.GuestMenu(choice, first_name)
            key=read_key()
        input()

    #СПИСОК КОМНАТ
    button_id_x = 1
    button_id_y = 1
    if choice == 'RoomsTable':
        key = 'w'
        while key != 'enter':
            if key == 'd' and button_id_y < 5:
                button_id_y += 1
            elif key == 'a' and button_id_y > 1:
                button_id_y -= 1
            elif key == 's' and button_id_x < 3:
                button_id_x += 1
            elif key == 'w' and button_id_x > 1:
                button_id_x -= 1
            Draw.RoomsTable(button_id_x, button_id_y)
            key = read_key()
        input()


    #СПИСОК ГОСТЕЙ
    if choice == 'GuestsList':
        while key != 'enter':
            # command = json.dumps({"command_name": "get_all_users"})
            # GuestsList = json.loads(ClientSession.message_handle(command))
            GuestsList = {
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
                }
            Draw.GuestsList()
            key = read_key()

    #СТАТУС ПРОЖИВАНИЯ
    if choice == 'GuestStatus':
        key = 'w'
        while key != 'enter':
            # command = json.dumps({"command_name": "get_all_users"})
            # GuestsList = json.loads(ClientSession.message_handle(command))
            Draw.GuestsList()
            key = read_key()

    #УПРАВЛЕНИЕ БРОНИРОВАНИЕМ
    input()
    if choice == 'RoomsTable':
        #command = json.dumps({"command_name": "get_rooms_list"})
        #RoomInfo = json.loads(ClientSession.message_handle(command))
        RoomInfo = {
                        'server_answer': 'Список комнат',
                        'rooms': [
                            {
                                'room_number': 1, # уникален для каждой комнаты
                                'room_floor': 2,
                                'occupied': False, # True - комната занята False - комната свободна
                                'room_resident': 'Liza', # ник человека проживающего в комнате (эти данные получает только админ),
                            },
                            {
                                'room_number': 4,
                                'room_floor': 1,
                                'occupied': True,  # True - комната занята False - комната свободна
                                'room_resident': 'John',  # ник человека проживающего в комнате (эти данные получает только админ)
                            }
                        ],
                        'answer_status': 'ok'
                    }
        login = ' '
        floor = button_id_x
        number = button_id_y
        occupied = False
        for room in RoomInfo['rooms']:
            if room['room_floor'] == button_id_x and room['room_number'] == button_id_y:
                login = json.dumps(room['room_resident'])
                floor = json.dumps(room['room_floor'])
                number = json.dumps(room['room_number'])
                occupied = json.dumps(room['occupied'])
                while key != 'enter':
                    Draw.ManageBooking(login, floor, number, occupied, is_admin)
                    if is_admin:
                        print("Введите команду: (1 - подтвердить бронь, 2 - отменить бронь, 3 - выселить)", end="")
                        task = input()
                        print("Введите причину", end="")
                        reason = input()
                        # if task == 1:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "confirm_reserve", "username": f"{login}", "reason": f"{reason}"}}})
                        # if task == 2:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "cansel_reserve", "username": f"{login}", "reason": f"{reason}"}}})
                        # if task == 3:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "kick_from_room", "username": f"{login}", "reason": f"{reason}"}}})
                    key = read_key()

            else:
                while key != 'enter':
                    Draw.ManageBooking(login, floor, number, occupied, is_admin)
                    if is_admin:
                        print("Введите команду: (1 - подтвердить бронь, 2 - отменить бронь, 3 - выселить)", end="")
                        task = input()
                        print("Введите причину", end="")
                        reason = input()
                        # if task == 1:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "confirm_reserve", "username": f"{login}", "reason": f"{reason}"}}})
                        # if task == 2:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "cansel_reserve", "username": f"{login}", "reason": f"{reason}"}}})
                        # if task == 3:
                        #     command = json.dumps({"command_name": "change_user_residence_status", "args": {{"change_type": "kick_from_room", "username": f"{login}", "reason": f"{reason}"}}})
                    key = read_key()


    #УВЕДОМЛЕНИЯ
    if choice == 'Notifications':
        key = 'w'
        while key != 'enter':
            # command = json.dumps({"command_name": "get_notifications"})
            # NotificationTitle = json.loads(ClientSession.message_handle(command))['notification_title']
            # NotificationDate = json.loads(ClientSession.message_handle(command))['notification_time']
            # Notification = json.loads(ClientSession.message_handle(command))['notification_text']
            NotificationTitle = 'Заголовок'
            NotificationDate = '21:43 09.03.2002'
            Notification = 'Пример уведомления'
            Draw.Notifications(NotificationTitle, NotificationDate, Notification)
            key = read_key()


