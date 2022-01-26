import sys
import json
import socket
import time
from common.variables import *
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):
    """
    Функция предназначена для генерации запроса о присутствии клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        },
    }
    return out


def process_answer(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: OK'
        return '400: Bad Request'
    raise ValueError


def main():
    """
    Загружаем параметы коммандной строки
    client.py 192.168.0.100 8079
    """
    try:
        server_address = sys.argv[2]
        server_port = int(sys.argv[3])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEF_IP_ADDRESS
        server_port = DEF_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_answer(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
