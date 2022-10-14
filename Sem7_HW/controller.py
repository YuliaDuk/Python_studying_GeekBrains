# Создать телефонный справочник с возможностью импорта и экспорта данных .
# Что должен уметь справочник?
# *  Добавить новый контакт
# * Поиск контакта по имени
# *Пример информации в справочнике:*
# Исаев Владислав Иванович || +3456789087565
# Наиль Н. || +45678987654

import model
import logger
import UI


def add_or_find():
    num = int(input('Если Вы хотите добавить контакт, введите 1.\nЕсли Вы хотите найти контакт, введите 2:\n'))
    if num == 1:
        answer = 0
        while answer != 'yes':
            name = UI.get_name()
            number = UI.get_number()
            print(f'Будет добавлен следующий контакт: {name} || {number}')
            answer = input('Если все верно, введите yes: ')
        UI.show_contact(name, number)
        logger.log_contact(name,number)
    elif num == 2:
        model.find_contact()

add_or_find()