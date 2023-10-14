
from rest_framework.views import APIView
from utils.common_response import APIResponse
from rest_framework import serializers
from utils.common_pagination import CommonPageNumberPagination
from django.db.models import Q # ORM 对 sql 的操作
from app.models import Roles
from app.serializer.RolesSerializers import RolesSerializers, RolesModelSerializers
from app.error.error import ERROR_CODE_1200, ERROR_CODE_1300, ERROR_CODE_1400, CommonError, RoleError


# 新增
class RoleInsertView(APIView):

    def post(self, request):

        # 使用POST接口获取参数
        data = request.data

        # 序列化和校验     传instance是编辑    只有data是新增 
        serializer = RolesSerializers(data=data)
        

        try:
            # raise_exception=True 参数是为了获取 RolesSerializers 内部的序列化的必填项和校验错误（内部和自定义）
            serializer.is_valid(raise_exception=True)
            # serializer.save()  是保存到数据库中   保存成功 返回字典对象 
            notice = serializer.save()

            # 字典对象不可直接返回    需要转化为 json
            response = RolesModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))


# 删除
class RoleDeleteView(APIView):

    def delete(self, request):

        # 获取 URL 上的参数
        id = request.query_params.get('id')
        # filter查找出所有为id的数据（可以是多个是一个QuerySet查询集），执行delete删除   返回删除的数量  
        # 物理删除
        # deleted_count, _ = Roles.objects.filter(id=id).delete()
        # deleted_count, _ = Roles.objects.get(id=id).delete()
        # if deleted_count == 0:
        #     return APIResponse(code=ERROR_CODE_1300, msg=RoleError.MSG_1300)
        # return APIResponse(body={ "id": id })

        # 逻辑删除
        role = Roles.objects.get(id=id)
        if role:
            role.isDelete = True
            role.save()
            response = RolesModelSerializers(instance=role)
            return APIResponse(body=response.data)
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=RoleError.MSG_1300)


# 编辑
class RoleUpdataView(APIView):

    def put(self, request):

        # 获取 id
        id = request.data.get('id')
        user_type = request.auth_user.type
        
        # 当前账号不能修改自己角色的权限
        if user_type == 2:
            user_role_id = request.auth_user_model["roleId"]
            if int(id) == user_role_id:
                return APIResponse(code=ERROR_CODE_1400, msg=CommonError.MSG_1400)

        # get查找出id的数据只有一个   没有执行引发 Roles.DoesNotExist
        try:
            role = Roles.objects.get(id=id)
        except Roles.DoesNotExist:
            return APIResponse(code=ERROR_CODE_1300, msg=RoleError.MSG_1300)

        # 序列化和校验     传instance是编辑    只有data是新增
        serializer = RolesSerializers(instance=role, data=request.data, partial=True)

        try:
            # raise_exception=True 参数是为了获取 RolesSerializers 内部的序列化的必填项和校验错误（内部和自定义）
            serializer.is_valid(raise_exception=True)
            # serializer.save()  是保存到数据库中   保存成功 返回字典对象 
            notice = serializer.save()

            # 字典对象不可直接返回    需要转化为 json
            response = RolesModelSerializers(instance=notice)
            return APIResponse(body=response.data)
        
        except serializers.ValidationError as e:
            return APIResponse(ERROR_CODE_1200, str(e))

       

# 获取列表
class RoleListView(APIView):
    
    # CommonPageNumberPagination 自定义分页
    pagination_class = CommonPageNumberPagination
    
    # self执行上下文，相当于this  request请求提
    def get(self, request):
        
        user_type = request.auth_user.type

        # 获取url参数  用作搜索
        name = request.query_params.get('name')
        page = request.query_params.get('page')  # 获取page参数
         
        # 查询所有isDelete为false的数据（没有软删除的数据）  使用 order_by 排序

        roles = Roles.objects.filter(Q(isDelete=False)).order_by('-id')

        user_type = request.auth_user.type

        # 当前账号不能获取自己角色的权限
        if user_type == 2:
            user_role_id = request.auth_user_model["roleId"]
            roles = roles.exclude(id=user_role_id)


        # 如果没有传递page参数，则返回全部数据
        if not page:
            response = RolesModelSerializers(instance=roles, many=True)
            return APIResponse(body=response.data)

        # 如果参数存在，根据参数进行过滤   name   __icontains   模糊搜索
        if name: 
            roles = roles.filter(Q(name__icontains=name))

        # 分页处理 指定 pagination_class 函数  获取分页字典对象
        paginator = self.pagination_class()

        """
            request.query_params.get() 第一个参数是要获取的key 第二个参数是没有对应key的value时候,设置一个默认值 
            获取传递的参数  self.pagination_class.page_size_query_param  自定的分页名称 
            重新设置没页的数量
        """ 
        page_size = request.query_params.get(self.pagination_class.page_size_query_param, self.pagination_class.page_size)  
        paginator.page_size = page_size

        """
            使用分页器对查询集进行分页处理。
            paginator.paginate_queryset(queryset, request)
            第一个参数queryset是查询集roles 或者列表 roles.values()   (roles.values()将查询集 roles 转换为一个字典的列表)
            第二个参数是包含分页参数的请求对象 (如：页码、每页条目数) 对查询集进行分页处理，并返回分页后的结果。
        """
        paginated_roles = paginator.paginate_queryset(roles, request)

        # 使用 RolesModelSerializers 序列化   many=True 是序列化多个   返回 json 对象
        response = RolesModelSerializers(paginated_roles, many=True)
        
        # 字典对象不能给直接返回给前端   需要json 一下
        body = {
            'total': paginator.page.paginator.count,  # 总条数
            'page': paginator.page.number,  # 当前页数
            'pageSize': int(paginator.page_size),  # 每页条数
            'list': response.data,  # 数据列表
        }

        return APIResponse(body=body)


# 获取详情
class RoleDetailView(APIView):

    def get(self, request):


        user_type = request.auth_user.type
        id = request.query_params.get('id')
        
        # 当前账号不能获取自己角色的权限
        if user_type == 2:
            user_role_id = request.auth_user_model["roleId"]
            if int(id) == user_role_id:
                return APIResponse(code=ERROR_CODE_1400, msg=CommonError.MSG_1400)

        try:
            role = Roles.objects.get(id=id)
            if role.isDelete:
                return APIResponse(code=ERROR_CODE_1300, msg=RoleError.MSG_1300)
        except Roles.DoesNotExist:
            return APIResponse(code=ERROR_CODE_1300, msg=RoleError.MSG_1300)

        response = RolesModelSerializers(instance=role)

        return APIResponse(body=response.data)



