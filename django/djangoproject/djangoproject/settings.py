"""
djangoproject项目的Django设置。
由“django-admin-startproject”使用django 4.2.2生成。

有关此文件的详细信息，请参阅
https://docs.djangoproject.com/en/4.2/topics/settings/

有关设置及其值的完整列表，请参见
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# 在项目内部构建路径，如下所示:BASE_DIR/“subdir”。
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速启动开发设置-不适合生产
# 请参阅https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 安全警告:对生产中使用的密钥保密！
SECRET_KEY = 'django-insecure-d111y=1ziukr07k*!r$q=zcgto%=9o^x9l-e74_78y_#0lle6a'

# 安全警告:不要在生产中打开调试的情况下运行！
DEBUG = True

ALLOWED_HOSTS = []


# Application definition 应用程序定义

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework", # 配置 rest_framework
    "corsheaders", # 跨域
    "app"
]


REST_FRAMEWORK = {
    # # 身份认证
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
    # # 权限认证
    # 'DEFAULT_PERMISSION_CLASSES': ('utils.permissions.CustomPermission',),
    # 分页
    'DEFAULT_PAGINATION_CLASS': 'utils.common_pagination.pagination_handler',
    # 自动生成文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 过滤
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 异常
    'EXCEPTION_HANDLER': 'utils.common_exceptions.exception_handler',
}

MIDDLEWARE = [

    # 自定义中间件 用来做登录认证  需要放到最上面
    'app.middleware.authentication_middleware.AuthTokenMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 跨域 中间件
    'corsheaders.middleware.CorsMiddleware', # 跨域
]

# 配置白名单  不进行登录验证
WHITELIST = [
    '/api/login',
]


# 允许所有的跨域请求
# CORS_ORIGIN_ALLOW_ALL = True
# 允许指定的域名进行跨域请求
CORS_ORIGIN_WHITELIST = [
  'http://localhost:9686',
]



ROOT_URLCONF = 'djangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproject.wsgi.application'


# Database 数据库
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'python',          # 数据库名称
        'USER': 'python',               # 数据库用户名
        'PASSWORD': '123456',           # 数据库密码
        'HOST': '127.0.0.1',                   # 数据库主机（本地为localhost）
        'PORT': '3306',                        # 数据库端口号
    }
}



# Password validation  密码验证
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization 国际化
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)  静态文件（CSS、JavaScript、Images）
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type 默认主键字段类型
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
