# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

import cProfile
import functools


def items_sum_loop(range_count):
    items_sum = 0
    item = 1
    while range_count > 0:
        items_sum += item
        item /= -2
        range_count -= 1
    return items_sum


cProfile.run('items_sum_loop(50)')


def items_sum_recursion(range_count, current_item=1.0):
    if range_count == 0:
        return 0
    elif range_count == 1:
        return current_item
    return current_item + items_sum_recursion(range_count - 1, current_item / -2)


cProfile.run('items_sum_recursion(50)')


def items_sum_m(range_count):
    func_dict = {0: 0, 1: 1, 2: 0.5}

    def _items_sum(_range_count, current_item=1.0):
        if _range_count in func_dict:
            return func_dict[_range_count]
        func_dict[_range_count] = current_item + _items_sum(_range_count - 1, current_item / -2)
        return func_dict[_range_count]

    return _items_sum(range_count)


cProfile.run('items_sum_m(50)')


@functools.lru_cache()
def items_sum_c(range_count, current_item=1.0):
    if range_count == 0:
        return 0
    elif range_count == 1:
        return current_item
    return current_item + items_sum_c(range_count - 1, current_item / -2)


cProfile.run('items_sum_c(50)')
