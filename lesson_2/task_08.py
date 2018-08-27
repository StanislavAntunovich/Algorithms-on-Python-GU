# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num_list = []

while True:
    num = input('Введите число (0 для завершения): ')
    if num == '0':
        break
    num_list.append(num)

digit_to_count = input('Введите цифру для подсчета: ')

digit_count = 0
num_list = ''.join(num_list)

for digit in num_list:
    if digit == digit_to_count:
        digit_count += 1

print(f'Цифра "{digit_to_count}" встречается {num_list.count(digit_to_count)} раз')
