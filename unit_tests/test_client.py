import unittest

from client import create_presence, process_answer
from common.variables import *


class TestClient(unittest.TestCase):
    """
    Класс с тестами для клиента (client.py)
    """

    def test_def_create_presence(self):
        test = create_presence()
        test[TIME] = 1.0
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_response(self):
        # тест разбора ответа 200
        self.assertEqual(process_answer({RESPONSE: 200}), '200: OK')

    def test_400_response(self):
        # тест разбора ответа 400
        self.assertEqual(process_answer({RESPONSE: 400}), '400: Bad Request')

    def test_no_response(self):
        # тест исключения без RESPONSE
        self.assertRaises(ValueError, process_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
