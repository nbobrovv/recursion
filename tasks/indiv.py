#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
При правильной расстановке выполняются условия:
количество открывающих и закрывающих скобок равно.
внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
расставлены правильно.
"""


def brackets_check(s):
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0


if __name__ == '__main__':
    if brackets_check(input('Введите строку: ')):
        print('True')
    else:
        print('False')
