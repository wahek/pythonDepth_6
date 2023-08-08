import all_pacage
import datetime
from datetime import date
from sys import argv

__all__ = ['ex_7_']


def ex_7_():
    day, month, year = input('Введи дату формата: ДД.ММ.ГГГГ\n').split('.')
    my_date = year + month + day
    try:
        datetime.datetime(int(year), int(month), int(day))
        print(ex_7.is_leap(int(year)))
        print(f'{date.fromisoformat(my_date)} Дата существует')
    except ValueError:
        print('Даты не существует')


def ex_7_console(args):
    day, month, year = args
    my_date = year + month + day
    try:
        datetime.datetime(int(year), int(month), int(day))
        print(all_pacage.ex_7.is_leap(int(year)))
        print(f'{date.fromisoformat(my_date)} Дата существует')
    except ValueError:
        print('Даты не существует')


if __name__ == '__main__':
    arg = argv[1:]
    ex_7_console(arg)
