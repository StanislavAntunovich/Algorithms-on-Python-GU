import random

LIMIT = 10
unsorted_array = [random.randint(-100, 99) for _ in range(LIMIT)]


def bubbles_reverse_sort(array):
    aim_array = array.copy()
    n = 1
    while n < len(aim_array):
        changed = False
        for i in range(len(aim_array) - n):
            if aim_array[i] < aim_array[i + 1]:
                aim_array[i], aim_array[i + 1] = aim_array[i + 1], aim_array[i]
                changed = True
        if not changed:
            return aim_array
        n += 1


if __name__ == '__main__':
    reverse_sorted_array = bubbles_reverse_sort(unsorted_array)
    print('unsorted', unsorted_array)
    print('sorted  ', reverse_sorted_array)
