# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter1 = input('Введите первую букву (латинскую): ')
letter2 = input('Введите вторую букву (латинскую): ')

STRING = ' abcdefghijklmnopqrstuvwxyz'

index1 = STRING.index(letter1)
index2 = STRING.index(letter2)

letters_between = abs(index1 - index2) - 1

print(
    f'Порядковый номер "{letter1}" = {index1} \n'
    f'Порядковый номер "{letter2}" = {index2} \n'
    f'между ними {letters_between} букв(а)'
)
