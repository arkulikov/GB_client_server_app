"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

var_1 = 'разработка'
var_2 = 'администрирование'
var_3 = 'protocol'
var_4 = 'standard'

my_list = [var_1, var_2, var_3, var_4]
my_list_after = []

for el in my_list:
    el_encode = el.encode('utf-8')
    print(f"После кодировки: {el_encode}, тип: {type(el_encode)}")
    my_list_after.append(el_encode)

for el in my_list_after:
    el_decode = el.decode('utf-8')
    print(f"После декодировки: {el_decode}, тип: {type(el_decode)}")
