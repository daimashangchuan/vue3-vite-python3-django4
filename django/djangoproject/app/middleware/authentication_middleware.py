from django.conf import settings
from utils.common_response import APIJsonResponse
from app.error.error import ERROR_CODE_1600, CommonError
from app.models import Users
from app.serializer.UsersSerializers import UsersModelSerializers
import jwt

class AuthTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 检查请求路径是否在白名单中
        if self.is_whitelisted(request.path):
            return self.get_response(request)

        # 验证请求 Headers 是否包含 HTTP_AUTH_TOKEN
        token = request.META.get('HTTP_AUTN_SJW_TOKEN')

        if token is None:
            return APIJsonResponse(code=ERROR_CODE_1600, msg=CommonError.MSG_1600)

        # 解码 JWT Token
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return APIJsonResponse(code=ERROR_CODE_1600, msg=CommonError.MSG_1600)

        # 构建查询条件
        condition = {
            'phone': decoded_token['phone'],
            'passWord': decoded_token['passWord'],
            'passWordMd5': decoded_token['passWordMd5'],
            # 'is_active': True,
        }
        # 查询数据
        auth_user = Users.objects.filter(**condition).first()

        auth_user_model = UsersModelSerializers(instance=auth_user)

        if auth_user:
            request.auth_user = auth_user
            request.auth_user_model = auth_user_model.data
            return self.get_response(request)
        else:
            return APIJsonResponse(code=ERROR_CODE_1600, msg=CommonError.MSG_1600)

    def is_whitelisted(self, path):
        # 检查请求路径是否在白名单中
        return any(path.startswith(pattern) for pattern in settings.WHITELIST)
