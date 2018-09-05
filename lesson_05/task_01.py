# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

firms_count = int(input('Введите количество предпиятий: '))
firms = {}
total_profit = 0

for firm in range(firms_count):
    firm_name = input(f'Введите название для {firm + 1} предпиятия: ')
    firms[firm_name] = 0

    for quoter in range(4):
        profit = float(input(f'Введите прибыль за {quoter + 1} квартал: '))
        total_profit += profit
        firms[firm_name] += profit

average_profit = total_profit / firms_count

lower_profit = [f for f in firms if firms[f] < average_profit]
higher_profit = [f for f in firms if firms[f] > average_profit]

print('Фирмы с прибылью выше среднего: ', end='')
print(*higher_profit, sep=', ')

print('Фирмы с прибылью ниже среднего: ', end='')
print(*lower_profit, sep=', ')
