
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import serializers
from utils.common_logger import logger

# 只要走到这个函数中，一定是出异常了 要记录日志
def exception_handler(exc, context):
    # 1.记录日志,哪个ip地址，用户id是多少，访问哪个路径，执行哪个视图函数，出了什么错
    request = context.get('request')
    view = context.get('view')
    ip = request.META.get('REMOTE_ADDR')

    user_id = request.auth_user.id

    path = request.get_full_path()
    logger.error('用户【%s】，ip地址为【%s】，访问地址为【%s】,执行的视图函数为【%s】，出错是【%s】'%(user_id,ip,path,str(view),str(exc)))
    response = drf_exception_handler(exc, context)
    if response:  
        status_code = response.status_code
        logger.warning('drf出了异常，异常是:%s' % str(status_code))
        # drf 的异常已经处理了 ---》直接取detail 会又小问题 遇到再解决
        logger.warning('drf出了异常，异常是:%s' % str(exc))
        res = Response({'code': status_code, 'msg': response.data.get('detail', '服务器异常，请联系系统管理员')})
    else:
        # django的异常,咱们要处理
        logger.error('用户【%s】，ip地址为【%s】，访问地址为【%s】,执行的视图函数为【%s】，出错是【%s】,总的错误是===========【%s】' % (user_id, ip, path, str(view), str(exc), str(context)))
        # 代码逻辑问题
        res = Response({'code': 500, 'msg': '服务器异常，请联系系统管理员' })

    return res
