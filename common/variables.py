# Порт по умолчанию
DEF_PORT = 7777
# IP по умолчанию
DEF_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключения
MAX_CONNECTION = 5
# Максимальная длина сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка
ENCODING = 'utf-8'

# Протоколы JIM (JSON instant messaging)
ACTION = 'action'
TIME = 'time'
RESPONSE = 'response'
ALERT = 'alert'
ERROR = 'error'
USER = 'user'
ACCOUNT_NAME = 'account_name'
# Присутствие. Сервисное сообщение для извещения сервера о присутствии клиента online
PRESENCE = 'presence'
# Проверка присутствия. Сервисное сообщение от сервера для проверки присутствии клиента online
PROBE = 'probe'
# Простое сообщение пользователю или в чат
MSG = 'msg'
# Отключение от сервера
QUIT = 'quit'
# Авторизация на сервере
AUTHENTICATE = 'authenticate'
# Присоединиться к чату
JOIN = 'join'
# Покинуть чат
LEAVE = 'leave'
