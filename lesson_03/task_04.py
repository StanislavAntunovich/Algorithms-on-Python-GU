# Определить, какое число в массиве встречается чаще всего.

import random

limit = 10
size = 300

array = [random.randint(-limit, limit) for _ in range(300)]

array_items_count = []
max_count = 0
needed_nums = set()

for i in array:
    count_i = 0
    for n in array:
        if i == n:
            count_i += 1
    array_items_count += [count_i]
    if count_i > max_count:
        max_count = count_i

for i, item in enumerate(array_items_count):
    if item == max_count:
        needed_nums.add(array[i])

print('число(а)', *needed_nums, f'всетречаются {max_count} раз')
