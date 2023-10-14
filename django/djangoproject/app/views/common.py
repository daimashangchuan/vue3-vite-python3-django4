# 请求方式 结合 路由as_view()视图
from rest_framework.views import APIView
from rest_framework import serializers
# ORM 对 sql 的操作
from django.db.models import Q

# models 数据
from app.models import Users

# 时间格式 # jwt生成/解码         # md5加密
import datetime; import jwt; import hashlib;

# 统一返回格式
from utils.common_response import APIResponse

# Users的序列化  增/删/改/查
from app.serializer.UsersSerializers import UsersSerializers, UsersModelSerializers

# 获取 setting 配置
from django.conf import settings



# 错误日志
from app.error.error import ERROR_CODE_1100, ERROR_CODE_1200, ERROR_CODE_1300, ErrorMsg, CommonError



# 登录
class LoginView(APIView):

    def post(self, request):
        # 从请求数据中获取用户名和密码
        phone = request.data.get('phone')
        passWord = request.data.get('passWord')
        passWordMd5 = request.data.get('passWordMd5')
        
        # 检查必传参数是否存在
        if not phone or not passWord or not passWordMd5:
            return APIResponse(code=ERROR_CODE_1100, msg=ErrorMsg.MSG_1100)

        # 构建查询条件
        condition = Q(phone=phone) & Q(passWord=passWord) & Q(passWordMd5=passWordMd5)
        # 查询数据
        user = Users.objects.filter(condition).first()

        if user is not None:
            # 用户已通过身份验证，生成 token
            expires_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            payload = {
                'phone': user.phone,
                'passWord': user.passWord,
                'passWordMd5': user.passWordMd5,
                'exp': expires_at
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            # 创建序列化器实例并验证数据
            serialized = UsersModelSerializers().to_representation(user)
            response = UsersModelSerializers(data=serialized, partial=True)
            response.is_valid()
            return APIResponse(body={'token': token, **response.data })
        else:
            # 身份验证失败
            return APIResponse(code=ERROR_CODE_1200, msg=CommonError.MSG_1200)



# 获取个人信息
class UserInfoView(APIView):

    def get(self, request):
        if request.auth_user:
            response = UsersModelSerializers(instance=request.auth_user)
            return APIResponse(body=response.data)
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=CommonError.MSG_1300)



# 修改个人信息
class UpdataView(APIView):

    def put(self, request):
        
        if request.auth_user:
            auth_user = request.auth_user
            serializer = UsersSerializers(instance=auth_user, data=request.data, partial=True)
            try:
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                # 字典对象不可直接返回    需要转化为 json
                response = UsersModelSerializers(instance=user)
                return APIResponse(body=response.data)
            except serializers.ValidationError as e:
                return APIResponse(ERROR_CODE_1200, str(e))
            
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=CommonError.MSG_1300)

        
# 修改密码
class UpdataPassView(APIView):

    def put(self, request):
        
        passWord = request.data.get('passWord')
        newPassWord = request.data.get('newPassWord')
        confirmNewPassWord = request.data.get('confirmNewPassWord')

        if request.auth_user:
            auth_user = request.auth_user
            if passWord != auth_user.passWord:
                return APIResponse(code=1500, msg='旧密码错误')
            if newPassWord != confirmNewPassWord:
                return APIResponse(code=1400, msg='俩次密码不一致')

            passWordMd5 = hashlib.md5(newPassWord.encode()).hexdigest()
            data = {
                "passWord": newPassWord,
                "passWordMd5": passWordMd5
            }
            # auth_user = Users.objects.get(id=auth_user.id) 
            serializer = UsersSerializers(instance=auth_user, data=data, partial=True)
            
            try:
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                # 字典对象不可直接返回    需要转化为 json
                response = UsersModelSerializers(instance=user)
                return APIResponse(body=response.data)
            except serializers.ValidationError as e:
                return APIResponse(ERROR_CODE_1200, str(e))
            
        else:
            return APIResponse(code=ERROR_CODE_1300, msg=CommonError.MSG_1300)


           


    








