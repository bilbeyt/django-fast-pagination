import unittest
from helpers import FastPaginator


class FastPaginatorTestMethods(unittest.TestCase):

    def test_queryset_valid(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(Exception):
            paginator = FastPaginator(example_list, 2)
            paginator.page(3)


if __name__ == '__main__':
    unittest.main()
