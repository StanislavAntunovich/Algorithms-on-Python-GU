import random


def make_array(limit, round_=None):
    """ :param round_ :type: int - число после запятой до которого округлять, по умолчанию не округлять,
        :param limit :type: list - длина массива
        :return массив """
    if not round:
        return [random.uniform(0, 49) for _ in range(limit)]
    return [round(random.uniform(0, 49), round_) for _ in range(limit)]


def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    first = merge_sort(array[:middle])
    second = merge_sort(array[middle:])
    return _merge(first, second)


def _merge(first, second):
    sorted_list = []
    while first and second:
        if first[0] < second[0]:
            sorted_list.append(first.pop(0))
        else:
            sorted_list.append(second.pop(0))
    if first:
        sorted_list.extend(first)
    if second:
        sorted_list.extend(second)
    return sorted_list


if __name__ == '__main__':
    unsorted_array = make_array(10, 2)
    sorted_array = merge_sort(unsorted_array)
    print('unsorted:', unsorted_array)
    print('sorted:  ', sorted_array)
