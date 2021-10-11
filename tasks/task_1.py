#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Самостоятельно изучите работу со стандартным пакетом Python timeit . Оцените с
помощью этого модуля скорость работы итеративной и рекурсивной версий функций
factorial и fib . Во сколько раз измениться скорость работы рекурсивных версий
функций factorial и fib при использовании декоратора lru_cache ? Приведите в отчет и
обоснуйте полученные результаты.
"""


from timeit import timeit


fib1 = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''
factorial1 = """
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)
"""
fib2 = """
def fib2(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
"""
fib3 = """
from functools import lru_cache
@lru_cache
def fib3(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib3(n - 2) + fib3(n - 1)
"""
factorial2 = """
def factorial2(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
"""
factorial3 = """
from functools import lru_cache
@lru_cache
def factorial3(n):
    if n == 0:
        return 1
    else:
        return n * factorial3(n-1)
"""
if __name__ == '__main__':
    print("Время выполнения рекрусивной функции числа Фибоначи: ",
          timeit(setup=fib1, number=1000))
    print("Время выполнения итеративной функции числа Фибоначи: ",
          timeit(setup=fib2, number=1000))
    print("Время выполнения рекрусивной функции числа Фибоначи с"
          " использованием декоратора lru_cache: ",
          timeit(setup=fib3, number=1000))
    print("Время выполнения рекрусивной функции факториала: ",
          timeit(setup=factorial1, number=1000))
    print("Время выполнения итеративной функции факториала: ",
          timeit(setup=factorial2, number=10000))
    print("Время выполнения рекрусивной функции факториала с"
          " использованием декоратора lru_cache: ",
          timeit(setup=factorial3, number=10000))
