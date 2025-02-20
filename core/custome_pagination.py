from math import ceil

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, _positive_int


class ListingPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, payload: dict, plain=False):
        """ this method overrided for implement listing through post request(request.data)   """
        page = self.page
        previous = page.previous_page_number() if page.has_previous() else None
        next = page.next_page_number() if page.has_next() else None
        page_size = self.get_page_size(self.request)
        pagination_response = {
            'page_size': page_size,
            'total_pages': ceil(
                page.paginator.count / page_size),
            'current_page': page.number,
            'total_entries': page.paginator.count,
            'next': next,
            'previous': previous
        }
        response = {
            "pagination": pagination_response,
            "data": payload
        }

        if plain:
            return response
        return Response(response)

    def get_page_number(self, request, paginator):
        """ this method overrided for implement listing through post request(request.data) """
        page_number = request.query_params.get(self.page_query_param, request.data.get(self.page_query_param, 1))
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def get_page_size(self, request):
        """ this method overrided for implement listing through post request(request.data)  """
        if self.page_size_query_param:
            try:
                return _positive_int(
                    request.query_params.get(self.page_size_query_param, request.data.get(self.page_size_query_param,
                                                                                          self.page_size)),
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size

    def get_limit(self, request):
        """ this method overrided for implement listing through post request(request.data)  """

        if self.limit_query_param:
            try:
                return _positive_int(
                    request.query_params.get(self.limit_query_param, request.data.get(self.limit_query_param,
                                                                                      self.default_limit)),
                    strict=True,
                    cutoff=self.max_limit
                )
            except (KeyError, ValueError):
                pass
