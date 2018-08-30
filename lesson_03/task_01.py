# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2, 100)]
delimiters = [i for i in range(2, 10)]

for i in delimiters:
    delim_list = []
    for n in array:
        if n % i == 0:
            delim_list += [n]
    print(f'{i} кратны:', *delim_list)
