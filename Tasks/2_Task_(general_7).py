#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit
from functools import lru_cache


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorail_iter(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return n


@lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_iter(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    start_time = timeit.default_timer()
    factorial(1000)
    print("Время, затраченное на выполнение factoruil (lru_cache): ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    factorial_rec(1000)
    print("Время, затраченное на выполнение factorial_rec: ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    factorail_iter(1000)
    print("Время, затраченное на выполнение factorail_iter: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    fib(1000)
    print("Время, затраченное на выполнение fib (lru_cache): ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib_rec(1000)
    print("Время, затраченное на выполнение fib_rec: ", timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    fib_iter(1000)
    print("Время, затраченное на выполнение fib_iter: ", timeit.default_timer() - start_time)
