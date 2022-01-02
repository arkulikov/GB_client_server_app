"""Функции для приема и отправки сообщений"""
import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(client):
    """
    Функция принимает и декодирует сообщение.
    Принимает байты, отдает словарь.
    Если передано что-то другое - возвращает ошибку
    """
    # recv - функция, отвечающая за получение данных
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    # isinstance - функция, позволяет проверить принадлженость экземпляра к классу
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        # load - функция, позволяющая преобразовать строку JSON в объект Python
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Функция для отправки и кодирования сообщения.
    Принимает словарь и отправляет его
    """
    # dumbs - функция, для преобразование данных Python в строку JSON
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    # send - функция, отвечаюшая за передачу данных
    sock.send(encoded_message)
