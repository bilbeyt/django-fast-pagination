from django.db.models.query import QuerySet


class InvalidPageNumberException(Exception):
    pass


class InvalidObjectListException(Exception):
    pass


class FastPaginator():
    def __init__(self, object_list, per_page):
        if not isinstance(object_list, QuerySet):
            raise InvalidObjectListException("Object list should be a Queryset")
        self.object_list = object_list
        self.per_page = per_page
        self.paginate()

    def paginate(self):
        self.ids = {obj['id'] for obj in self.object_list.values('id')}
        self.ids = list(self.ids)
        self.count = len(self.ids)
        self.pages = []
        for i in range(0, self.count, self.per_page):
            self.pages.append(self.ids[i:i+self.per_page])
        self.number_of_pages = len(self.pages)

    def page(self, number):
        number = self.validate_number(number)
        return self.object_list.filter(id__in=self.pages[number-1])

    def validate_number(self, number):
        if isinstance(number, float) and not number.is_integer():
            raise InvalidPageNumberException("Page number should be an integer")
        if isinstance(number, str) and not number.isdigit():
            raise InvalidPageNumberException("Page number should be an integer")
        number = int(number)
        if number < 1:
            raise InvalidPageNumberException(
                "Page number should be a positive integer")
        if number > self.number_of_pages:
            raise InvalidPageNumberException("Page Does Not Exist")
        return number

