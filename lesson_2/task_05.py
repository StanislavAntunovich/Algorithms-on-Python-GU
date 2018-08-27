# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.


def ascii_table(start_index, end_index, pair_count=1):
    if start_index == end_index:
        return f'{start_index} - "{chr(start_index)}" '
    else:
        if pair_count % 10 == 0:
            return f'{start_index} - "{chr(start_index)}" ' + '\n' + ascii_table(start_index + 1, end_index,
                                                                                 pair_count + 1)
        else:
            return f'{start_index} - "{chr(start_index)}" ' + ascii_table(start_index + 1, end_index, pair_count + 1)


print(ascii_table(32, 127))
