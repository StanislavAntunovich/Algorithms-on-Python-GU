# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

size = 30
limit = 15

array = [random.randint(-limit, limit) for _ in range(size)]
print(array)

min1 = array[0]
min1_pos = 0

min2 = array[0]
min2_pos = 0

for i, v in enumerate(array):
    if v < min1:
        min1 = v
        min1_pos = i

for i, v in enumerate(array):
    if (v < min2 or v == min1) and i != min1_pos:
        min2 = v
        min2_pos = i

print(f'Минимальные значения: {min1} и {min2}')
