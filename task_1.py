"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений или другого инструмента
извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных
данных в соответствующий CSV-файл;
"""
import csv

os_prod_list, os_name_list, os_code_list, os_type_list, header_list = [], [], [], [], []


def fill_lists(file_name, param_name, list_name=[], h_list=[]):
    with open(file_name, encoding='utf-8') as f_n:
        for line in f_n:
            if line.find(param_name) != -1:
                my_str = line.split(':')
                list_name.append(my_str[1].strip())
                header_list.append(my_str[0].strip())


def get_data():
    main_list = []

    for i in range(1, 4):
        fill_lists(f'info_{i}.txt', 'Изготовитель системы:', os_prod_list, header_list)
        fill_lists(f'info_{i}.txt', 'Название ОС:', os_name_list, header_list)
        fill_lists(f'info_{i}.txt', 'Код продукта:', os_code_list, header_list)
        fill_lists(f'info_{i}.txt', 'Тип системы:', os_type_list, header_list)

    main_list.append(header_list[0:4])
    j = 1
    for i in range(0, 3):
        row_data = []
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_list.append(row_data)
        j += 1

    return main_list


def write_to_csv(csv_file):
    main_data = get_data()

    with open(csv_file, 'w', encoding='utf-8') as file:
        write = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            write.writerow(row)


write_to_csv('main_csv.csv')
