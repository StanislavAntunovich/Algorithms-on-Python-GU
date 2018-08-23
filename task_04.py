# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

range_min = input('Введите минимальное значение диапазона: ')
range_max = input('Введите максимальное значение диапазона: ')

if range_min.isalpha() and range_max.isalpha():
    STRING = 'abcdefghijklmnopqrstuvwxyz'
    min_index = STRING.index(range_min)
    max_index = STRING.index(range_max)
    random_letter = random.choice(STRING[min_index:max_index + 1])
    print(f'Случайная буква из диапазона от "{range_min}" до "{range_max}" -> {random_letter}')

elif '.' in range_min and '.' in range_max:
    print(
        f'Случайное вещественное число из диапазона от "{range_min}" до "{range_max}" -> '
        f'{random.uniform(float(range_min), float(range_max))}'
    )

# Пердполагаем, что пользователь идеальный и не смешивает букы и числа.
else:
    print(
        f'Случайное целое число из диапазона от "{range_min}" до "{range_max}" -> '
        f'{random.randint(int(range_min), int(range_max))}'
    )


