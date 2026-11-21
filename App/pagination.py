from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPadination(PageNumberPagination):
    page_size=100
    page_size_query_param='size'
    max_page_size=200