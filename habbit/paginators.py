from rest_framework.pagination import PageNumberPagination


class HabbitPagination(PageNumberPagination):
    """Пагинация страниц с ограниченным кол-вом объектов на странице"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 25
