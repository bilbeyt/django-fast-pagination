import unittest
from fast_pagination.helpers import FastPaginator
from django.core.paginator import InvalidPage, PageNotAnInteger, EmptyPage


class FastObjectPaginatorTestMethods(unittest.TestCase):

    def test_invalid_page(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(InvalidPage):
            paginator = FastPaginator(
                example_list, 2,
                cache_key="invalid_page_test_key")
            paginator.page(3)

    def test_page_not_an_integer(self):
        example_list = ['1', '2', '3']
        with self.assertRaises(PageNotAnInteger):
            paginator = FastPaginator(
                example_list, 2,
                cache_key="not_integer_test_key")
            paginator.page(None)

    def test_page_empty(self):
        example_list = []
        with self.assertRaises(EmptyPage):
            paginator = FastPaginator(
                example_list, 2,
                cache_key="empty_page_test_key")
            paginator.page(-1)

    def test_key_not_found(self):
        example_list = []
        with self.assertRaises(ValueError):
            paginator = FastPaginator(
                example_list, 2)


if __name__ == '__main__':
    unittest.main()
