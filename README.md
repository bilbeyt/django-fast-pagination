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
