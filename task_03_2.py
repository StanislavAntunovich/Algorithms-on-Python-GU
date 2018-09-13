import random


def make_array(m):
    return [random.randint(-100, 99) for _ in range(2 * m + 1)]


# Есть недостаток - не найдет медиану если ее численное значение не в единственном экземпляре
def median_search(array):
    for n in array:
        if len([i for i in array if i < n]) == len([i for i in array if i > n]):
            return n
    return 'численное значение медианы не в единственном экземпляре... работаю над решением'


# Вариант II, имеет тот же недостаток.
def median_search_m(array):
    random_item = random.choice(array)
    less = [i for i in array if i < random_item]
    more = [i for i in array if i > random_item]
    if len(less) == len(more):
        return random_item
    if len(less) > len(more):
        less, more = more, less
    for n in more:
        if len([i for i in array if i < n]) == len([i for i in array if i > n]):
            return n
    return 'численное значение медианы не в единственном экземпляре... работаю над решением'


if __name__ == '__main__':
    unsorted_array = make_array(4)
    median = median_search_m(unsorted_array)
    median2 = median_search(unsorted_array)
    print('unsorted:', unsorted_array)
    print('sorted:  ', sorted(unsorted_array))
    print('median:', median)
    print('median v.2:', median2)

#