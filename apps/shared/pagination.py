from rest_framework.pagination import PageNumberPagination


class CourseCategoryPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3

# and add some paginations

# write some data
# and every pagination should 10