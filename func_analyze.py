import sys


class AnalyzeMemoDecorator(object):
    def __init__(self, func):
        self._locals = {}
        self.func = func

    def _get_size(self, x):
        total_mem = sys.getsizeof(x)

        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for y in x.items():
                    total_mem += sys.getsizeof(y)
            elif not isinstance(x, str):
                for y in x:
                    total_mem += sys.getsizeof(y)
        return total_mem

    def _analyze_func(self):
        _vars = {}
        for key in self._locals:
            _vars[key] = self._get_size(self._locals[key])
        total_mem = sum(_vars.values())

        for var, mem_size in _vars.items():
            print(f'Переменная "{var}" занимает {mem_size}')
        print(f'Всего памяти занято перменными: {total_mem}')

    def __call__(self, *args, **kwargs):

        def tracer(frame, event, arg):
            if event == 'return':
                self._locals = frame.f_locals.copy()

        sys.setprofile(tracer)
        res = self.func(*args, **kwargs)
        sys.setprofile(None)
        self._analyze_func()

        return res
