# test_app.py

import unittest
from app import lower_case, upper_case, length_string

class TestStringFunctions(unittest.TestCase):
    def test_lower_case(self):
        self.assertEqual(lower_case('HELLO'), 'hello')
        self.assertEqual(lower_case('World'), 'world')
        self.assertEqual(lower_case('123'), '123')
        self.assertEqual(lower_case(''), '')

    def test_upper_case(self):
        self.assertEqual(upper_case('hello'), 'HELLO')
        self.assertEqual(upper_case('World'), 'WORLD')
        self.assertEqual(upper_case('123'), '123')
        self.assertEqual(upper_case(''), '')

    def test_length_string(self):
        self.assertEqual(length_string('hello'), 5)
        self.assertEqual(length_string(''), 0)
        self.assertEqual(length_string(' '), 1)
        self.assertEqual(length_string('1234'), 4)

if __name__ == '__main__':
    unittest.main()
