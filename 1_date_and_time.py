"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime 


def print_days():
    dt = datetime.date.today()
    delta = datetime.timedelta(days=1)
    calc_date = dt - delta
    print(f'Вчера было {calc_date}')
    print(f'Сегодня {dt}')
    delta = datetime.timedelta(days=30)
    calc_date = dt - delta
    print(f'30 дней назад было {calc_date}')


def str_2_datetime(date_string):
    dt = datetime.datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
    return dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
