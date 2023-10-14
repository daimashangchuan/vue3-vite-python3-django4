from rest_framework.views import APIView
from utils.common_response import APIResponse
from rest_framework import serializers
from app.serializer.NoticesSerializers import NoticesSerializers, NoticesModelSerializers
from app.error.error import ERROR_CODE_1200, ERROR_CODE_1300, NoticeError
from app.models import Notices
from utils.common_pagination import CommonPageNumberPagination
from django.db.models import Q

# 新增
class NoticeInsertView(APIView):

    def post(self, request):

        data = request.data
        serializer = NoticesSerializers(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            notice = serializer.save()
            response = NoticesModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))


# 删除
class NoticeDeleteView(APIView):

    def delete(self, request):

        id = request.query_params.get('id')
        notice = Notices.objects.get(id=id)
        if notice:
            notice.isDelete = True
            notice.save()
            response = NoticesModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=NoticeError.MSG_1300)


# 编辑
class NoticeUpdataView(APIView):

    def put(self, request):

        id = request.data.get('id')

        try:
            notice = Notices.objects.get(id=id)
        except:
            return APIResponse(ERROR_CODE_1300, NoticeError.MSG_1300)

        serializer = NoticesSerializers(instance=notice, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            notice = serializer.save()
            response = NoticesModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))

# 列表
class NoticeListView(APIView):

    pagination_class = CommonPageNumberPagination

    def get(self, request):

        name = request.query_params.get('name')
        page = request.query_params.get('page')  # 获取page参数

        notice = Notices.objects.filter(Q(isDelete=False)).order_by('-id')

        if not page:
            response = NoticesModelSerializers(instance=notice, many=True)
            return APIResponse(body=response.data)

        if name:
            notice = notice.filter(Q(name__icontains=name))

        paginator = self.pagination_class()
        page_size = request.query_params.get(self.pagination_class.page_size_query_param, self.pagination_class.page_size)  
        paginator.page_size = page_size
        paginated_notice = paginator.paginate_queryset(notice, request)

        response = NoticesModelSerializers(paginated_notice, many=True)

        # 字典对象不能给直接返回给前端   需要json 一下
        body = {
            'total': paginator.page.paginator.count,  # 总条数
            'page': paginator.page.number,  # 当前页数
            'pageSize': int(paginator.page_size),  # 每页条数
            'list': response.data,  # 数据列表
        }

        return APIResponse(body=body)


# 详情
class NoticeDetailView(APIView):

    def get(self, request):

        id = request.query_params.get('id')
        notice = Notices.objects.get(id=id)
        
        if notice.isDelete:
                return APIResponse(code=ERROR_CODE_1300, msg=NoticeError.MSG_1300)
        
        response = NoticesModelSerializers(instance=notice)
        return APIResponse(body=response.data)




