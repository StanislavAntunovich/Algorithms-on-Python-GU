# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections
from script_analyze import analyze

firms_count = int(input('Введите количество предпиятий: '))
firms_profit = collections.Counter()

for firm in range(firms_count):
    firm_name = input(f'Введите название для {firm + 1} предпиятия: ')
    firms_profit[firm_name] = 0

    for quoter in range(4):
        profit = float(input(f'Введите прибыль за {quoter + 1} квартал: '))
        firms_profit[firm_name] += profit

average_profit = sum(firms_profit.values()) / firms_count

lower_profit = [f for f in firms_profit if firms_profit[f] < average_profit]
higher_profit = [f for f in firms_profit if firms_profit[f] > average_profit]

print('Фирмы с прибылью выше среднего: ', end='')
print(*higher_profit, sep=', ')

print('Фирмы с прибылью ниже среднего: ', end='')
print(*lower_profit, sep=', ')

if __name__ == '__main__':

    analyze(globals())
