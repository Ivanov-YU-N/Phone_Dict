main_menu = '''
 Ukfdyjt vty.
 1.Открыть файл
 2.Сохранить файл
 3.Показать все контакты
 4.Создать новый контакт
 5.Найти контакт
 6.Изменить контакт
 7.Удалить контакт
 8.Вывод
 '''
menu_choice = 'Выберите пункт меню'
input_error = 'Некоректный ввод'
book_error = 'телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'
input_new_contact = 'Введите данные нового контакта'
new_contakt = ['Введите имя контакта:', 'Введите телефон:', 'Введите коментарий:']
input_index = 'Введите индекс изменяемого контакта'
input_change_contact = 'Введите данные изменяемого контакта или Enter? чтоб оставить без изменений: '
search_word = 'Введите искомый элемент'

def contact_saved(name: str):
    return f'контакт {name} успешное сохранение'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'
