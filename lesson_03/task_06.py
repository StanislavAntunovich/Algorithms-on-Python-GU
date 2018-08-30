# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 10
limit = size ** 2

array = [random.randint(-limit, limit) for _ in range(size)]

nums_sum = 0

min_num = array[0]
min_num_pos = 0

max_num = array[0]
max_num_pos = 0

for index, value in enumerate(array):
    if value > max_num:
        max_num = value
        max_num_pos = index

    if value < min_num:
        min_num = value
        min_num_pos = index

if min_num_pos > max_num_pos:
    for i in range(max_num_pos + 1, min_num_pos):
        nums_sum += array[i]
else:
    for i in range(min_num_pos + 1, max_num_pos):
        nums_sum += array[i]

print(f'Сумма между минимальным ({min_num}) и максимальным ({max_num}) равна {nums_sum}')
