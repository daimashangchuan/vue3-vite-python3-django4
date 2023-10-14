from rest_framework.views import APIView
from utils.common_response import APIResponse
from rest_framework import serializers
from app.serializer.UsersSerializers import UsersSerializers, UsersModelSerializers
import hashlib
from app.error.error import ERROR_CODE_1200, ERROR_CODE_1300, UserError
from app.models import Users
from utils.common_pagination import CommonPageNumberPagination
from django.db.models import Q

# 新增
class UserInsertView(APIView):

    def post(self, request):

        data = request.data
        phone = request.data.get('phone')
        passWord = phone[-6:]
        passWordMd5 = hashlib.md5(passWord.encode()).hexdigest()
        data['passWord'] = passWord
        data['passWordMd5'] = passWordMd5
        data['type'] = 2

        serializer = UsersSerializers(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            notice = serializer.save()
            # 字典对象不可直接返回    需要转化为 json
            response = UsersModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))


# 删除
class UserDeleteView(APIView):

    def delete(self, request):

        id = request.query_params.get('id')
        user = Users.objects.get(id=id)
        if user:
            user.isDelete = True
            user.save()
            response = UsersModelSerializers(instance=user)
            return APIResponse(body=response.data)
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=UserError.MSG_1300)


# 编辑
class UserUpdataView(APIView):

    def put(self, request):

        id = request.data.get('id')

        try:
            user = Users.objects.get(id=id)
        except:
            return APIResponse(ERROR_CODE_1300, UserError.MSG_1300)
        
        serializer = UsersSerializers(instance=user, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            notice = serializer.save()
            # 字典对象不可直接返回    需要转化为 json
            response = UsersModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))
        
            

# 列表
class UserListView(APIView):

    pagination_class = CommonPageNumberPagination

    def get(self, request):

        name = request.query_params.get('name')
        phone = request.query_params.get('phone')
        page = request.query_params.get('page')  # 获取page参数


        if request.auth_user.id:
            id = request.auth_user.id
            user = Users.objects.filter(Q(isDelete=False) & Q(type=2) & ~Q(id=id)).order_by('-id')
        else:
            user = Users.objects.filter(Q(isDelete=False) & Q(type=2)).order_by('-id')

        if not page:
            response = UsersModelSerializers(instance=user, many=True)
            return APIResponse(body=response.data)

        if name:
            user = user.filter(name__icontains=name)
        if phone:
            user = user.filter(phone__icontains=phone)

        paginator = self.pagination_class()
        page_size = request.query_params.get(self.pagination_class.page_size_query_param, self.pagination_class.page_size)  
        paginator.page_size = page_size
        paginated_user = paginator.paginate_queryset(user, request)
        
        response = UsersModelSerializers(instance=paginated_user, many=True)

        # 字典对象不能给直接返回给前端   需要json 一下
        body = {
            'total': paginator.page.paginator.count,  # 总条数
            'page': paginator.page.number,  # 当前页数
            'pageSize': int(paginator.page_size),  # 每页条数
            'list': response.data,  # 数据列表
        }

        return APIResponse(body=body)


# 详情
class UserDetailView(APIView):

    def get(self, request):

        id = request.query_params.get('id')

        if request.auth_user.id:
            auth_user_id = request.auth_user.id
            if auth_user_id == id:
                return APIResponse(code=ERROR_CODE_1300, msg=UserError.MSG_1300)

        user = Users.objects.filter(id=id).first()
        if user.isDelete:
                return APIResponse(code=ERROR_CODE_1300, msg=UserError.MSG_1300)
        
        print('++++++++++++++')
        print(user)
        print('++++++++++++++')

        response = UsersModelSerializers(instance=user)
        return APIResponse(body=response.data)




