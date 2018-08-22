# По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

x1 = float(input('Введите значение x координаты для первой точки: '))
y1 = float(input('Введите значение y координаты для первой точки: '))
x2 = float(input('Введите значение x координаты для второй точки: '))
y2 = float(input('Введите значение y координаты для второй точки: '))

if x1 == x2 or y1 == y2:
    print('решений нет')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение прямой проходящей через точки A({x1}, {y1}) и B({x2}, {y2}) -> y = {k}x + {b}')
