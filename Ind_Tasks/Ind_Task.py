#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def clear_str(stri):
    """
    Удаление лишних символов.
    """
    res = ""
    for s in stri:
        if s in "()[]":
            res = res + s
    return res


def check_par(stri):
    """
    Проверка правильности расстановки скобок.
    """
    if len(stri) == 0:
        return True
    else:
        a = stri[0]
        b = stri[-1]
        s = "([".find(a)
        if s == -1:
            return False
        if b == ")]"[s]:
            return check_par(stri[1:len(stri) - 1])
        else:
            return False


def main():
    """""
    Главная функция программы.
    """""
    strk = input("Введите строку: ")
    check_par(clear_str(strk))


if __name__ == '__main__':
    main()
