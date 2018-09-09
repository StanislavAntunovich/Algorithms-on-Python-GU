# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.

from func_analyze import AnalyzeMemoDecorator


@AnalyzeMemoDecorator
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


if __name__ == '__main__':
    print(prime_num_e(5))
