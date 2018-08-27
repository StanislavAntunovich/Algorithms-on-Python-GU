# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.


def check_formula(n):
    num_sum = 0
    for i in range(1, n + 1):
        num_sum += i
    if num_sum == n * (n + 1) / 2:
        return True
    return False


print(check_formula(546))
