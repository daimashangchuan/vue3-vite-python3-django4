"""
djangoproject项目的ASGI配置。
它将可调用的ASGI公开为名为“application”的模块级变量。
有关此文件的详细信息，请参阅
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

application = get_asgi_application()
