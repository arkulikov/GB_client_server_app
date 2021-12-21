"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

PING = 'ping'
YA = 'yandex.ru'
YOUTUBE = 'youtube.com'

yandex_ping = subprocess.Popen([PING, YA], stdout=subprocess.PIPE)

print("PING YANDEX.RU")

for el in yandex_ping.stdout:
    result = chardet.detect(el)
    print(result)
    el = el.decode(result['encoding']).encode('utf-8')
    print(el.decode('utf-8'))

print("PING YOUTUBE.COM")

youtube_ping = subprocess.Popen([PING, YOUTUBE], stdout=subprocess.PIPE)

for el in youtube_ping.stdout:
    result = chardet.detect(el)
    print(result)
    el = el.decode(result['encoding']).encode('utf-8')
    print(el.decode('utf-8'))
