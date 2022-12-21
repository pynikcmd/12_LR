#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа показыает работу декоратора, который производит оптимизацию
# хвостового вызова. Он делает это, вызывая исключение, если оно является его
# прародителем, и перехватывает исключения, чтобы вызвать стек.

import sys
import timeit


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    # Эта программа показывает работу декоратора, который производит оптимизацию
    # хвостового вызова. Он делает это, вызывая исключение, если оно является его
    # прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.
    # Эта функция не работает, если функция декоратора не использует хвостовой вызов.

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
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


def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


def fib(i, current=0, nextt=1):
    if i == 0:
        return current
    else:
        return fib(i - 1, nextt, current + nextt)


@tail_call_optimized
def factorial_optimized(n, acc=1):
    if n == 0:
        return acc
    return factorial_optimized(n - 1, n * acc)


@tail_call_optimized
def fib_optimized(i, current=0, nextt=1):
    if i == 0:
        return current
    else:
        return fib_optimized(i - 1, nextt, current + nextt)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    fib(100)
    print("Время на выполнение factoruil: ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib(100)
    print("Время на выполнение оптимизированной factorial_optimized: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    fib(100)
    print("Время на выполнение fib: ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib_optimized(100)
    print("Время на выполнение оптимизированной fib_optimized: ", timeit.default_timer() - start_time)
