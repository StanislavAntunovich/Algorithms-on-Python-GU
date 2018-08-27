# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_list = []

while True:
    num = input('Введите число (0 для завершения): ')
    if num == '0':
        break
    num_list.append(num)

max_count = 0
needed_num = 0

for num in num_list:
    digit_count = 0

    for digit in num:
        digit_count += int(digit)

    if digit_count > max_count:
        max_count = digit_count
        needed_num = int(num)

print(f'Число "{needed_num}" с наибольшей суммой цифр = "{max_count}"')
