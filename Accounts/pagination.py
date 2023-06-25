from rest_framework import pagination

# from rest_framework.pagination import _positive_int
# from rest_framework.response import Response

# CustomPagination : 

class CustomPagination(pagination.PageNumberPagination) : 
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = None
    page_query_param = "page"
    # def paginate_queryset(self, queryset, request, view=None):
    #     """
    #     Paginate a queryset if required, either returning a
    #     page object, or `None` if pagination is not configured for this view.
    #     """
    #     self.count = self.get_count(queryset)
    #     page_size = self.get_page_size(request)
    #     if not page_size:
    #         return None

    #     paginator = self.django_paginator_class(queryset, page_size)
    #     page_number = self.get_page_number(request, paginator)

    #     try:
    #         self.page = paginator.page(page_number)
    #     except InvalidPage as exc:
    #         msg = self.invalid_page_message.format(
    #             page_number=page_number, message=str(exc)
    #         )
    #         raise NotFound(msg)

    #     if paginator.num_pages > 1 and self.template is not None:
    #         # The browsable API should display pagination controls.
    #         self.display_page_controls = True

    #     self.request = request
    #     return list(self.page)
    
    # def get_page_size(self, request):
    #     if self.page_size_query_param:
    #         try : 
    #             if request.query_params[self.page_size_query_param] == "all"  : 
    #                 return  _positive_int(
    #                 self.count,
    #                 strict=True,
    #                 cutoff=self.max_page_size
    #             ) 
    #         except (KeyError, ValueError):
    #             pass
    #         try:
    #             return _positive_int(
    #                 request.query_params[self.page_size_query_param],
    #                 strict=True,
    #                 cutoff=self.max_page_size
    #             )
    #         except (KeyError, ValueError):
    #             pass

    #     return self.page_size
    # def get_count(self, queryset):
    #     """
    #     Determine an object count, supporting either querysets or regular lists.
    #     """
    #     try:
    #         return queryset.count()
    #     except (AttributeError, TypeError):
    #         return len(queryset)
    # def get_paginated_response(self, data):
    #     return Response({
    #   'meta': {
    #     'next': self.get_next_link(),
    #     'previous': self.get_previous_link(),
    #     'count': self.page.paginator.count
    #   },
    #   'results': data
    # })
