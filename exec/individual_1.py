#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Поле first — целое положительное число, часы; поле second — целое
положительное число, минуты. Реализовать метод
minutes() — приведение времени в минуты.
'''


class Time:

    def __init__(self, first=0, second=0):
        first = int(first)
        second = int(second)
        print("Итоговое количество минут:", self.minutes(first, second))

    def minutes(self, first, second):
        return first * 60 + second


def is_valid(argument):
    if isinstance(argument, int) and argument >= 0:
        return True
    else:
        return False


def make_time(hours, minutes):
    if is_valid(hours) and is_valid(minutes):
        return Time(hours, minutes)
    else:
        print("[ERROR] Ошибка обработки данных")
        exit(1)


if __name__ == "__main__":
    time = make_time(input("Введите количество часов: "),
                     input("Введите количество минут: "))
    time.__init__
