#  Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

# Тоже самое, но функционально

from collections import Counter
from operator import itemgetter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, value):
        self.left.walk(code, value + '0')
        self.right.walk(code, value + '1')

    def __str__(self):
        return f'left "{self.left}, right {self.right}"'


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, value):
        code[self.char] = value


def _make_leaves(obj: str):
    new_counted = {}
    for key, val in dict(Counter(obj)).items():
        new_counted[Leaf(key)] = val
    return list(new_counted.items())


def huff_encode(string_):
    items = _make_leaves(string_)
    while len(items) >= 2:
        left_leaf = items.pop()
        right_leaf = items.pop()
        leaf_count = left_leaf[1] + right_leaf[1]
        items.append((MyNode(left=left_leaf[0], right=right_leaf[0]), leaf_count))
        items.sort(key=itemgetter(1), reverse=True)
    _node = items.pop()[0]
    code = {}
    _node.walk(code, '')
    print(code)
    for i in string_:
        print(code[i], end=' ')


if __name__ == '__main__':
    huff_encode('абра кадабра швабра')
