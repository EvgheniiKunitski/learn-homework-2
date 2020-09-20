"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

future_table = [
    {'name': 'Заповедникъ ЗОЖ', 'age': 40, 'job': 'Овоще база'},
    {'name': 'Capaldi', 'age': 25, 'job': 'бот'},
    {'name': 'Neznajka bot', 'age': 40, 'job': 'просто бот'},
    {'name': 'Alienspain', 'age': 40, 'job': 'Писатель'},
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]


def main():
    with open('table.csv', 'w', encoding='utf-8') as csv_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()
        for line in future_table:
            writer.writerow(line)


if __name__ == "__main__":
    main()
