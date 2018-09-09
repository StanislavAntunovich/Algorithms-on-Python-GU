import sys
import types


def _get_size(x):
    total_mem = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                total_mem += sys.getsizeof(y)
        elif not isinstance(x, str):
            for y in x:
                total_mem += sys.getsizeof(y)
    return total_mem


def analyze(global_vars: dict):
    """ Отсеивает глобальные переменные, выводит на экран информацию по каждой и общую занимаемую ими память,
        после выполнения кода.
        :param: :type: dict, в качестве параметра передавать globals() или словарь нужных переменных
    """
    _buf = global_vars
    _vars = {}
    for key in _buf:
        if not isinstance(_buf[key], (types.ModuleType, types.FunctionType)) and not key.startswith('__'):
            _vars[key] = _get_size(_buf[key])

    print('=' * 50)
    for key, value in _vars.items():
        print(f'Переменная "{key}" занимает {value}')
    print(f'Всего памяти занято перменными: {sum(_vars.values())}')
    print('=' * 50)
