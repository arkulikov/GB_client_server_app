"""Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

data_for_write = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_price': {'computer': '2000€-10000€',
                           'printer': '1000€-3000€',
                           'keyboard': '15€-150€',
                           'mouse': '17€-22€'}
           }

with open('file.yaml', 'w', encoding='utf-8') as file_in:
    yaml.dump(data_for_write, file_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file.yaml", 'r', encoding='utf-8') as file_out:
    data_for_out = yaml.load(file_out, Loader=yaml.SafeLoader)

print(data_for_write == data_for_out)
