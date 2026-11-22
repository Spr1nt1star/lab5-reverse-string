import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):

    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("level"), "level")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_cyrillic(self):
        self.assertEqual(reverse_string("Привет"), "тевирП")

    def test_digits_and_symbols(self):
        self.assertEqual(reverse_string("123!@#"), "#@!321")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_invalid_type_none(self):
        with self.assertRaises(TypeError):
            reverse_string(None)


if __name__ == "__main__":
    unittest.main()
