# Задача 38:
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# с семинара:
import os
phones_path=os.path.basename('C:/GB_DM/python_sem/phones.txt')

def all_contacts():
    with open(phones_path, 'r', encoding='utf8') as data:
        for line in data:
            print(line)
# all_contacts()

def find_contact(name):
    with open(phones_path, 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)
# find_contact('Петр')

def add_contact(new_contact):
    with open(phones_path, 'a', encoding='utf8') as data:
        data.write('\n')
        data.write(new_contact)


# ДЗ - продолжение
def del_contact(name):
    with open(phones_path, 'r', encoding='utf8') as data:
        lines_red=data.readlines()
    with open(phones_path, 'w', encoding='utf8') as data:
        for line in lines_red:
            if name not in line.strip('\n'):
                data.write(line)
    print('готово')
# del_contact('Федор')

def change_contact(name1, name1new):
    with open(phones_path, 'r', encoding='utf8') as data:
        lines_red=data.read()
    with open(phones_path, 'w', encoding='utf8') as data:
        lines_red=lines_red.replace(name1, name1new)
        data.write(lines_red)
    print('готово')
# change_contact('Петр Петров +79991231213', 'Петр Петров +89991231213')

def main_menu(num):
    if num == 1:
        all_contacts()
    elif num == 2:
        name = input('Введите искомое имя/фамилию/номер: ')
        find_contact(name)
    elif num == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
    elif num == 4:
        name = input('Введите имя/фамилию/номер для удаления: ')
        del_contact(name)
    elif num == 5:
        name_old = input('Введите имя,фамилию,номер для изменения: ')
        name_new = input('Введите НОВЫЙ имя,фамилию,номер: ')
        change_contact(name1, name2)

while True:
    print('Введите ')
    print('1 - для печати всего справочника; ')
    print('2 - для поиска контакта; ')
    print('3 - для записи контакта; ')
    print('4 - для изменения данных; ')
    print('5 - для удаления данных;')
    print('6 - для выхода из программы. ')
    num=int(input())
    if num == 6:
        break
    main_menu(num)

