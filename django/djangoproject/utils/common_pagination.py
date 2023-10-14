


from rest_framework.pagination import PageNumberPagination

class CommonPageNumberPagination(PageNumberPagination):
  page_size = 10 # 不传 默认一次取 10 条
  page_size_query_param = 'pageSize' # ?page=xx&pageSize=??
  min_page_size = 1 # 一次最多取 100 条
  max_page_size = 100 # 一次最多取 100 条

