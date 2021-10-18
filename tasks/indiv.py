#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
При правильной расстановке выполняются условия:
количество открывающих и закрывающих скобок равно.
внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
расставлены правильно.
"""


def check_brackets(string):
    left = string.find("(")
    right = string.rfind(")")
    if left == -1 and right == -1:
        return True
    elif left == -1 or right == -1 or right < left:
        return False
    else:
        return check_brackets(string[left + 1:right])


if __name__ == '__main__':
    if check_brackets(input("Введите скобочную последовательность: ")):
        print('True')
    else:
        print('False')
