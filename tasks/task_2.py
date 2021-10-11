#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Самостоятельно проработайте пример с оптимизацией хвостовых вызовов в Python. С
помощью пакета timeit оцените скорость работы функций factorial и fib с
использованием интроспекции стека и без использования интроспекции стека. Приведите
полученные результаты в отчет.
"""


from timeit import timeit


code1 = """
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
"""
code2 = """
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
"""
code3 = """
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
"""
code4 = """
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
"""
if __name__ == '__main__':
    print("Время выполнения функции factorial(): ",
          timeit(setup=code1, number=10000))
    print("Время выполнения функции factorial() c"
          " использованием интроспекции стека: ",
          timeit(setup=code3, number=10000))
    print("Время выполнения функции fib(): ",
          timeit(setup=code2, number=10000))
    print("Время выполнения функции fib() c"
          " использованием интроспекции стека: ",
          timeit(setup=code4, number=10000))
