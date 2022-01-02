import socket
import json
import sys
from common.variables import *
from common.utils import get_message, send_message


def process_client_message(message):
    """
    Функция для обработки сообщений от клиентов, принимает словарь - сообщение от клиента, проверяет корректность,
    возвращает словарь-ответ для клиента.
    """
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {
            RESPONSE: 200,
            ALERT: 'OK'}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Функция для загрузка параметров командной строки. Если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.0.100
    :return:
    """
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEF_PORT
        if 1024 > listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # указываем, какой IP-адрес слушать
    try:
        if '-a' in sys.argv:
            listen_address = int(sys.argv[sys.argv.index('-a') + 1])
        else:
            listen_address = ''
    except IndexError:
        print('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # создаем сокет
    # функция socket() - запускает создание сокета, AF_INET, — оно указывает, что создаваемый сокет будет сетевым
    # SOCK_STREAM указывает на то, что сокет работает с TCP-пакетами
    transport_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # функция bind() - привязать сокет к IP-адресу и порту машины
    transport_socket.bind((listen_address, listen_port))

    # слушаем порт
    # функция listen() сигнализирует о готовности принимать соединения
    transport_socket.listen(MAX_PACKAGE_LENGTH)
    while True:
        # функция accept() - принимает запрос на установку соединения
        client, client_address = transport_socket.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
