![Issues](https://img.shields.io/github/issues/bilbeyt/django-fast-pagination)
![Forks](https://img.shields.io/github/forks/bilbeyt/django-fast-pagination)
![Stars](https://img.shields.io/github/stars/bilbeyt/django-fast-pagination)
![License](https://img.shields.io/github/license/bilbeyt/django-fast-pagination)
![Twitter](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fbilbeyt%2Fdjango-fast-pagination)


## Fast Paginator for Django
Simple speedy pagination over your large database tables.

## Features

**Simple Integration**

FastPaginator API is compatible with Django's built-in pagination library. Only change your import statements then you're ready.

**Better SQL Queries**

Django's built-in pagination system builds SQL queries that have offset and limit clauses. FastPagination does not use them.

**Built-in Cache System**

FastPaginator has a built-in cache system. It does not cache QuerySets but caches primary keys of object lists. This provides speedup for pagination progress.

## Quick Start

1. Add "fast_pagination" to your INSTALLED_APPS setting like this:
```python
    INSTALLED_APPS = [
        ... 
        'fast_pagination'
    ]
```
2. In Django settings, you can set FAST_PAGINATION_TIMEOUT variable to invalidate cache. Default value is 1 hour.
3. In Django settings, you can set FAST_PAGINATION_PREFIX variable to use in cache keys. Default values is 'fastpagination'.
4. Import FastPaginator like this:
```python
    from fast_pagination.helpers import FastPaginator
```
5. Then, you are ready. All you have to do is give your queryset and number of entries when creating FastPaginator object.

## To Run Tests

1. Create a dummy project.
2. Run following command.
```python
./manage.py test fast_pagination.tests
```

## Benchmark

This benchmark is executed on Postgres9.6 with a table that has 1000000 rows, and fetched only one field. Results can be seen below.

| Paginator     | Min              | Max              | Mean             | StdDev        | Median           |
|---------------|------------------|------------------|------------------|---------------|------------------|
| Django        | 93.5535 (1.53) | 95.7217 (1.54) | 94.7340 (1.53) | 0.9755 (2.32) | 94.9046 (1.54) |
| FastPaginator | 61.1488 (1.0)   | 62.3316 (1.0)    | 61.7489 (1.0)    | 0.4205 (1.0)  | 61.7649 (1.0)    |


You can also run benchmark tests following instructions:

1. Run migrations if app needs using
```bash
./manage.py migrate
```
2. Call generate_users command from command line using
```bash
./manage.py generate_users 1000000
```
3. Run tests using
```bash
pytest fast_pagination/tests.py
```