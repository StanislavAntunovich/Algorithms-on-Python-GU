# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib.

from hashlib import sha1

string = input('Введите строку: ')

str_len = len(string)
sub_len = 1

sub_strings = []

while str_len > 1:
    for i in range(str_len):
        sub = sha1(string[i:i + sub_len].encode('utf-8')).hexdigest()
        if sub not in sub_strings:
            sub_strings.append(sub)
    sub_len += 1
    str_len -= 1

print(f'В строке "{string}" {len(sub_strings)} уникальных подстрок')
