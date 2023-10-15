from rest_framework import pagination

class VehiclePaginator(pagination.PageNumberPagination):
    page_size = 5
