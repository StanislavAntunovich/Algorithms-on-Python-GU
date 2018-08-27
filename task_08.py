# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

nums = ''

while True:
    num = input('Введите число (0 для завершения): ')
    if num == '0':
        break
    nums += num

digit_to_count = input('Введите цифру для подсчета: ')

digit_count = 0

for digit in nums:
    if digit == digit_to_count:
        digit_count += 1

print(f'Цифра "{digit_to_count}" встречается {nums.count(digit_to_count)} раз')
