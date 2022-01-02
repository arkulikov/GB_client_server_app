import unittest

from client import create_presence, process_answer
from server import *
from common.variables import *


class TestServer(unittest.TestCase):
    """
    Класс для тестирования сервера (server.py)
    """
    error_dict = {RESPONSE: 400, ERROR: 'Bad Request'}
    ok_dict = {RESPONSE: 200, ALERT: 'OK'}

    def test_no_action(self):
        # тест отсутствия action
        self.assertEqual(process_client_message({TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_wrong_action(self):
        # тест неправильный action
        self.assertEqual(process_client_message({ACTION: 'wrong', TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}}), \
                         self.error_dict)

    def test_no_time(self):
        # тест отстутствия TIME
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}),\
                         self.error_dict)

    def test_no_user(self):
        # тест отсутствия USER
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.0}), self.error_dict)

    def test_unkn_user(self):
        # тест - неизвестный USER
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest1'}}), \
                         self.error_dict)

    def test_ok(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}}), \
                         self.ok_dict)


if __name__ == '__main__':
    unittest.main()
