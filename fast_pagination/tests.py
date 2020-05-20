import unittest
from fast_pagination.helpers import FastPaginator
from django.core.paginator import InvalidPage, PageNotAnInteger, EmptyPage


class FastPaginatorTestMethods(unittest.TestCase):

    def test_invalid_page(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(InvalidPage):
            paginator = FastPaginator(example_list, 2)
            paginator.page(3)

    def test_page_not_an_integer(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(PageNotAnInteger):
            paginator = FastPaginator(example_list, 2)
            paginator.page(None)

    def test_page_empty(self):
        example_list = []
        with self.assertRaises(EmptyPage):
            paginator = FastPaginator(example_list, 2)
            paginator.page(-1)


if __name__ == '__main__':
    unittest.main()
