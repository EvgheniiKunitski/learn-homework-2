"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import sys


def main():
    one_string = ''
    with open('referat2.txt', 'w', encoding='utf-8') as result_file:
        with open('referat.txt', 'r', encoding='utf-8') as initial_file:
            for line in initial_file:
                one_string = one_string + line
                result_file.write(line.replace('.','!'))
    
    str_length = len(one_string)
    print(str_length)
    no_sintax_string = one_string.replace('.',' ').replace(',',' ').replace('/n',' ').replace('!',' ').replace('?',' ').replace(';',' ').replace(':',' ')
    count_words = len(no_sintax_string.split())
    print(count_words)



if __name__ == "__main__":
    main()
