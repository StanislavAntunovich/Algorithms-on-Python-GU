# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

import collections

indexes = {}
a = list('0123456789ABCDEF')
for value, key in enumerate(a):
    indexes[key] = value

print('Сегодня будем только складывать.')
num1 = list(input('Введите первое число: ').upper())
num2 = list(input('Введите второе число: ').upper())

sum_result = collections.deque()
buffer = collections.deque()


def hex_sum(a1, a2):
    buf = ''
    if not a2:
        return buf, a1
    index = indexes[a1] + indexes[a2]
    if index > 15:
        buf = '1'
        index -= 16
    return buf, a[index]


if len(num1) > len(num2):
    num1, num2 = num2, num1

delta_len = len(num2) - len(num1)
for _ in range(delta_len):
    num1.insert(0, '0')

for _ in range(len(num1)):
    buff2 = ''
    first, second = num1.pop(), num2.pop()
    buff, res = hex_sum(first, second)
    if buffer:
        sec = buffer.pop()
        buff2, res = hex_sum(res, sec)
    if buff:
        buffer.appendleft(buff)
    if buff2:
        buffer.appendleft(buff2)
    sum_result.appendleft(res)

if buffer:
    sum_result.appendleft(buffer.pop())

print(list(sum_result))
