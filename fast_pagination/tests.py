import unittest

import logging
import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import (
    InvalidPage, PageNotAnInteger, EmptyPage, Paginator)

from fast_pagination.helpers import FastPaginator



logger = logging.getLogger(__name__)


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


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'paginator',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }


def speed_test(queryset, paginator_cls):
    paginator = paginator_cls(queryset, 1000)
    for page in paginator.page_range:
        objs = paginator.page(page).object_list\
            .values_list('username', flat=True)
        usernames = ",".join(objs)
        logger.info("%s\n", usernames)


@pytest.mark.django_db
def test_django_paginator_speed(benchmark):
    queryset = User.objects.all()
    benchmark(speed_test, queryset, Paginator)


@pytest.mark.django_db
def test_fast_paginator_speed(benchmark):
    queryset = User.objects.all()
    benchmark(speed_test, queryset, FastPaginator)


if __name__ == '__main__':
    unittest.main()
