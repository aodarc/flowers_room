from rest_framework.pagination import PageNumberPagination


class OneResultPerPagePaginator(PageNumberPagination):
    page_size = 1

