# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = 10
limit = 10

array = [random.randint(-limit, limit) for _ in range(size)]
negative_array = []

for i in array:
    if i < 0:
        negative_array += [i]

max_from_negative = negative_array[0]
poses = []

for i in negative_array:
    if i > max_from_negative:
        max_from_negative = i

for i, item in enumerate(negative_array):
    if item == max_from_negative:
        poses += [i]

print(f'максимальное из отрицательных: {max_from_negative} на позиции(ях):', end=' ')
print(*poses, sep=', ')
