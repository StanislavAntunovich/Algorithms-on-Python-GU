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

# 100 loops, best of 3: 1.5 usec per loop - 10 раз
# 100 loops, best of 3: 2.73 usec per loop - 20 раз
# 100 loops, best of 3: 5.2 usec per loop - 40 раз
# линейная сложность

# cProfile.run('items_sum_loop(10)')
# # 1    0.000    0.000    0.000    0.000 task_01.py:7(items_sum_loop)
# cProfile.run('items_sum_loop(20)')
# # 1    0.000    0.000    0.000    0.000 task_01.py:7(items_sum_loop)
# cProfile.run('items_sum_loop(40)')
# # 1    0.000    0.000    0.000    0.000 task_01.py:7(items_sum_loop)


def items_sum_recursion(range_count, current_item=1.0):
    if range_count == 0:
        return 0
    elif range_count == 1:
        return current_item
    return current_item + items_sum_recursion(range_count - 1, current_item / -2)

# 100 loops, best of 3: 2.5 usec per loop - 10
# 100 loops, best of 3: 4.78 usec per loop - 20
# 100 loops, best of 3: 9.39 usec per loop - 40
# линейная сложность

# cProfile.run('items_sum_recursion(10)')
# # 10/1    0.000    0.000    0.000    0.000 task_01.py:26(items_sum_recursion)
# cProfile.run('items_sum_recursion(20)')
# # 20/1    0.000    0.000    0.000    0.000 task_01.py:26(items_sum_recursion)
# cProfile.run('items_sum_recursion(40)')
# # 40/1    0.000    0.000    0.000    0.000 task_01.py:26(items_sum_recursion)


def items_sum_m(range_count):
    func_dict = {0: 0, 1: 1, 2: 0.5}

    def _items_sum(_range_count, current_item=1.0):
        if _range_count in func_dict:
            return func_dict[_range_count]
        func_dict[_range_count] = current_item + _items_sum(_range_count - 1, current_item / -2)
        return func_dict[_range_count]

    return _items_sum(range_count)

# 100 loops, best of 3: 3.28 usec per loop - 10
# 100 loops, best of 3: 6.04 usec per loop - 20
# 100 loops, best of 3: 12.2 usec per loop - 40
# линейная сложность

# cProfile.run('items_sum_m(10)')
# # 9/1    0.000    0.000    0.000    0.000 task_01.py:46(_items_sum)
# cProfile.run('items_sum_m(20)')
# # 19/1    0.000    0.000    0.000    0.000 task_01.py:46(_items_sum)
# cProfile.run('items_sum_m(40)')
# # 39/1    0.000    0.000    0.000    0.000 task_01.py:46(_items_sum)


@functools.lru_cache()
def items_sum_c(range_count, current_item=1.0):
    if range_count == 0:
        return 0
    elif range_count == 1:
        return current_item
    return current_item + items_sum_c(range_count - 1, current_item / -2)

# 100 loops, best of 3: 0.147 usec per loop - 10
# 100 loops, best of 3: 0.147 usec per loop - 20
# 100 loops, best of 3: 0.14 usec per loop - 40
# линейная сложность

# cProfile.run('items_sum_c(10)')
# # 10/1    0.000    0.000    0.000    0.000 task_01.py:66(items_sum_c)
# cProfile.run('items_sum_c(20)')
# # 20/1    0.000    0.000    0.000    0.000 task_01.py:66(items_sum_c)
# cProfile.run('items_sum_c(40)')
# # 40/1    0.000    0.000    0.000    0.000 task_01.py:66(items_sum_c)
