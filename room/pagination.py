from rest_framework.pagination import PageNumberPagination


class RoomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
