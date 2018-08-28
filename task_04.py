# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

range_count = int(input('Введите длину последовательности: '))
items_sum = 0
item = 1

while range_count > 0:
    items_sum += item
    item /= -2
    range_count -= 1

print(f'Сумма элементов ряда равна {items_sum}')


# Вариант 2
def items_summ_count(items_count, current_item=1):
    if items_count == 1:
        return current_item
    elif items_count == 0:
        return 0
    else:
        return current_item + items_summ_count(items_count - 1, start_item / -2)
    
    
print(items_summ_count(5))
