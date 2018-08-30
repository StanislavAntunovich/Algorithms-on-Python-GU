# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

limit = 10
size = 30

nums_array = [random.randint(-limit, limit) for _ in range(size)]
indexes_array = []
# print(*nums_array)

for i, elem in enumerate(nums_array):
    if elem % 2 == 0:
        indexes_array += [i]

print('Индексы четных чисел: ', *indexes_array)
