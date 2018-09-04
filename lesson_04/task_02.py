# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile


# С решетом Эратосфена
def prime_num_e(index):
    if index == 1:
        return 2
    limit = index ** 2
    sieve = [i for i in range(limit + 1)]
    sieve[1] = 0

    for i in range(2, limit + 1):
        if sieve[i] != 0:
            j = i * 2
            while j < limit:
                sieve[j] = 0
                j += i
    prime_nums = [i for i in sieve if i != 0]
    return prime_nums[index - 1]


# cProfile.run('prime_num_e(50)')
# 1    0.001    0.001    0.002    0.002 task_02.py:8(prime_num_e)
# cProfile.run('prime_num_e(100)')
# 1    0.004    0.004    0.005    0.005 task_02.py:8(prime_num_e)
# cProfile.run('prime_num_e(200)')
# 1    0.020    0.020    0.024    0.024 task_02.py:8(prime_num_e)

# 100 loops, best of 3: 29.1 usec per loop - 10
# 100 loops, best of 3: 127 usec per loop - 20
# 100 loops, best of 3: 565 usec per loop - 40

# сложность O(4n)


# Без решета
def prime_nums_not_e(index):
    if index == 1:
        return 2
    num = 3
    prime_nums = [2]
    prime_nums_count = 0

    while prime_nums_count < index + 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_nums += [num]
            prime_nums_count += 1
        num += 1
    return prime_nums[index - 1]

# cProfile.run('prime_nums_not_e(50)')
# # 1    0.001    0.001    0.001    0.001 task_02.py:33(prime_nums_not_e)
# cProfile.run('prime_nums_not_e(100)')
# # 1    0.002    0.002    0.002    0.002 task_02.py:33(prime_nums_not_e)
# cProfile.run('prime_nums_not_e(200)')
# # 1    0.009    0.009    0.009    0.009 task_02.py:33(prime_nums_not_e)

# 100 loops, best of 3: 27.8 usec per loop - 10
# 100 loops, best of 3: 82.3 usec per loop - 20
# 100 loops, best of 3: 293 usec per loop - 40

# сложность O(4n)
