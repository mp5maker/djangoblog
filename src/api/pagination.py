from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)

# POST [LIMITOFFSETPAGINATION :: REST FRAMEWORK]
class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 2

# POST [PAGENUMBERPAGINATION :: REST FRAMEWORK]
class PostPageNumberPagination(PageNumberPagination):
    page_size = 2