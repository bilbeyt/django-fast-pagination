import unittest
from helpers import (
    FastPaginator, InvalidObjectListException)


class FastPaginatorTestMethods(unittest.TestCase):

    def test_queryset_valid(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(InvalidObjectListException):
            FastPaginator(example_list, 2)


if __name__ == '__main__':
    unittest.main()
