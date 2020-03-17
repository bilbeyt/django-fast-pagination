import inspect

from django.core.paginator import Paginator, Page
from django.db.models.query import QuerySet
from django.utils.functional import cached_property
from django.utils.inspect import method_has_no_args


class FastPaginator(Paginator):

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        if isinstance(object_list, QuerySet):
            self.ids = list(object_list.values_list('id', flat=True))

    @cached_property
    def count(self):
        c = getattr(self.object_list, 'count', None)
        if callable(c) and not inspect.isbuiltin(c) \
            and method_has_no_args(c) \
            and not isinstance(self.object_list, QuerySet):
            return c()
        return len(self.ids)

    def page(self, number):
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        object_list = self.object_list[bottom:top]
        if isinstance(self.object_list, QuerySet):
            ids = self.ids[bottom:top]
            object_list = self.object_list.filter(id__in=ids)
        return self._get_page(object_list, number, self)

    def _get_page(self, *args, **kwargs):
        return FastPage(*args, **kwargs)


class FastPage(Page):

    def __len__(self):
        return len(self.paginator.ids)
