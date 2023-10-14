
from rest_framework.response import Response
from django.http import JsonResponse

# 以后都使用自己封装的response
class APIResponse(Response):

    def __init__(self, code=0, msg='成功', body=(), status=200, headers=None, content_type=None, **kwargs):
        
        data = { 'code': code, 'msg': msg }
        if body:
            data['body'] = body
        super().__init__(data=data, status=status,
                         template_name=None, headers=headers,
                         exception=False, content_type=content_type)
        
    def __call__(self, *args, **kwargs):
        return self

class APIJsonResponse(JsonResponse):
    def __init__(self, code=0, msg='成功', body=(), status=200, headers=None, content_type=None, **kwargs):
        data = {'code': code, 'msg': msg}
        if body:
            data['body'] = body
        else:
            data['body'] = None
        super().__init__(data=data, status=status, safe=False, json_dumps_params={'ensure_ascii': False}, headers=headers, content_type=content_type)

    def __call__(self, *args, **kwargs):
        return self

