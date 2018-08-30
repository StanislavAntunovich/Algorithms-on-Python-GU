# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

rows = 5
columns = 7
min_limit = -2
max_limit = 12

matrix = [[random.randint(min_limit, max_limit) for _ in range(columns)] for _ in range(rows)]

for i in matrix:
    print(i)

columns_min = [i for i in matrix[0]]

for row in matrix:
    for i, item in enumerate(row):
        if item < columns_min[i]:
            columns_min[i] = item

max_from_mins = columns_min[0]

for i in columns_min:
    if i > max_from_mins:
        max_from_mins = i

print(f'"{max_from_mins}" максимальное из минимальных значений столбцов')
