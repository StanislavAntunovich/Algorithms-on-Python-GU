# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
limit = size ** 2

array = [random.randint(-limit, limit) for _ in range(size)]
print('Первоначальный: ', array)

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

array[min_num_pos], array[max_num_pos] = array[max_num_pos], array[min_num_pos]

print('После замены: ', array)
