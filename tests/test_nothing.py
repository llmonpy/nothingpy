# tests/test_nothing.py

import unittest
from src.nothingpy import Nothing, NothingClass


class TestNothing(unittest.TestCase):

    def setUp(self):
        self.nothing1 = Nothing
        self.nothing2 = NothingClass()

    def test_bool(self):
        self.assertFalse(bool(self.nothing1))

    def test_str(self):
        self.assertEqual(str(self.nothing1), "")

    def test_len(self):
        self.assertEqual(len(self.nothing1), 0)

    def test_iter(self):
        self.assertEqual(list(iter(self.nothing1)), [])

    def test_repr(self):
        self.assertEqual(repr(self.nothing1), "Nothing")

    def test_values(self):
        self.assertEqual(list(self.nothing1.values()), [])

    def test_keys(self):
        self.assertEqual(list(self.nothing1.keys()), [])

    def test_items(self):
        self.assertEqual(list(self.nothing1.items()), [])

    def test_eq_nothing(self):
        self.assertEqual(self.nothing1, self.nothing2)

    def test_eq_none(self):
        self.assertEqual(self.nothing1, None)

    def test_eq_false(self):
        self.assertEqual(self.nothing1, False)

    def test_not_eq_true(self):
        self.assertNotEqual(self.nothing1, True)

    def test_not_eq_zero(self):
        self.assertNotEqual(self.nothing1, 0)

    def test_not_eq_empty_string(self):
        self.assertNotEqual(self.nothing1, "")

    def test_not_eq_other_object(self):
        class Other:
            pass

        other = Other()
        self.assertNotEqual(self.nothing1, other)


if __name__ == '__main__':
    unittest.main()
