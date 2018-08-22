# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_index = int(input('Введите порядковый номер буквы латинского алфавита: '))

STRING = ' abcdefghijklmnopqrstuvwxyz'

letter = STRING[letter_index]

print(f'Ваша буква -> "{letter}"')

