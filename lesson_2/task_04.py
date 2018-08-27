# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

range_count = int(input('Введите длину последовательности: '))
items_sum = 0
item = 1

while range_count > 0:
    items_sum += item
    item /= -2
    range_count -= 1

print(f'Сумма элементов ряда равна {items_sum}')
