from django.db.models.query import QuerySet
from django.core.paginator import Paginator


class FastPaginator(Paginator):

    def page(self, number):
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        object_list = self.object_list[bottom:top]
        if isinstance(self.object_list, QuerySet):
            ids = self.object_list.values_list('id', flat=True)
            object_list = self.object_list.filter(id__in=ids)
        return self._get_page(object_list, number, self)
