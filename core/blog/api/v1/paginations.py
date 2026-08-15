from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """
    This class for custom the pagination for the post blog
    """

    page_size = 2

    def get_paginated_response(self, data):
        """
        Make the pre and next url of pagination and show the
        number of the total obj and total page
        """
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "total_obj": self.page.paginator.count,
                "total_page": self.page.paginator.num_pages,
                "results": data,
            }
        )
