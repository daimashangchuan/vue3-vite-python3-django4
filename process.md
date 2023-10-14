## 创建一个 django 项目

```
python              3.11.0
Django              4.2.2
django-cors-headers 4.0.0
djangorestframework 3.14.0
pyjwt               2.7.0
PyMySQL             1.0.3
```

### 创建独立运行环境  pythonproject 虚拟环境  
```
python3 -m venv 项目名
生成目录   目录 / bin  include  lib  pyvenv.cfg
          bin 目录下有  python3、pip3  执行文件

cd 项目名/bin
运行虚拟环境 mac笔记本 source activate 
Windows用activate.bat  用来激活 venv 环境



cd 项目名/bin 所有的安装都是在  项目名/bin 下安装
安装 django
pip3 install django 或者 pip3 install django==3

cd ..  && cd ..
安装 django项目
django-admin  startproject djangoproject


创建 app 
cd djangoproject
python3 manage.py startapp app名称
  migrations      迁移记录  不用需改  自动生成
    __init.py__  
  admin.py        内部管理后台的配置（不用）
  apps.py         不用修改
  models.py       数据库，类->sql语句（ORM） py类转化为sql语句
  tests.py        单元测试
  views.py        视图函数


## 运行django项目
cd djangoproject
python3 manage.py runserver  运行项目 或者  python3 manage.py runserver 8000 指定端口


```



### 修改配置 setting.py
```
## 修改为中文
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

找到 setting.py  MIDDLEWARE
将'django.middleware.csrf.CsrfViewMiddleware',  注释 (使用自定义的校验方式)
django.middleware.csrf.CsrfViewMiddleware 是 Django 的中间件之一，用于处理跨站请求伪造（CSRF）保护。当开启 CSRF 保护时，该中间件会验证每个 POST 请求的 CSRF 标记，以防止恶意网站利用用户的身份执行恶意操作。
```

## 链接数据库 在项目中修改 setting.py
```
需要在虚拟环境安装    pip3 install pymysql
在 setting.py 文件 或者 __init__.py  添加 （使用的版本问题）
  import pymysql
  pymysql.version_info = (1, 4, 6, "final", 0)  # 模拟 mysqlclient 版本信息
  pymysql.install_as_MySQLdb()

在 INSTALLED_APPS: {} 添加 app项目 web

修改 DATABASES 链接本地数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'python',          # 数据库名称
        'USER': 'python',               # 数据库用户名
        'PASSWORD': '123456',           # 数据库密码
        'HOST': '127.0.0.1/',                   # 数据库主机（本地为localhost）
        'PORT': '3306',                        # 数据库端口号
    }
}
```

## 在 app项目中的 models.py 建立模型
```
python3 manage.py makemigrations
python3 manage.py migrate  

创建好类型执行 python3 manage.py makemigrations  用于生成 Django 项目中的数据库迁移文件
当修改了 Django 项目中的模型（Models）时，需要运行 makemigrations 命令来生成相应的数据库迁移文件

AutoField: 自动递增的整数字段。
  primary_key (布尔值，默认为 False): 指定该字段是否为主键。

TextField: 长文本字段。 / CharField: 字符串字段。
  max_length (整数值): 指定字段的最大长度。
  null (布尔值，默认为 False): 指定字段是否允许为空。
  blank (布尔值，默认为 False): 指定字段在表单中是否可以为空白。
  default (值): 指定字段的默认值。


IntegerField: 整数字段。 / FloatField: 浮点数字段。
  null (布尔值，默认为 False): 指定字段是否允许为空。
  blank (布尔值，默认为 False): 指定字段在表单中是否可以为空白。
  default (值): 指定字段的默认值。

BooleanField: 布尔字段。
  null (布尔值，默认为 False): 指定字段是否允许为空。
  blank (布尔值，默认为 False): 指定字段在表单中是否可以为空白。
  default (值): 指定字段的默认值。
DateField、DateTimeField 和 TimeField:

DateField: 日期字段。 / DateTimeField: 日期时间字段。 / TimeField: 时间字段。
  null (布尔值，默认为 False): 指定字段是否允许为空。
  blank (布尔值，默认为 False): 指定字段在表单中是否可以为空白。
  auto_now (布尔值，默认为 False): 指定字段在每次保存时是否自动更新为当前日期/时间。
  auto_now_add (布尔值，默认为 False): 指定字段在创建对象时是否自动设置为当前日期/时间。
  default (值): 指定字段的默认值。

EmailField: 电子邮件字段。 / URLField: URL字段。
  max_length (整数值): 指定字段的最大长度。
  null (布尔值，默认为 False): 指定字段是否允许为空。
  blank (布尔值，默认为 False): 指定字段在表单中是否可以为空白。

FileField: 文件上传字段。
ImageField: 图像上传字段。
ForeignKey: 外键字段，用于建立模型之间的关联关系。
ManyToManyField: 多对多关系字段。

```


## 跨域问题
```
pip3 install django-cors-headers
在 Django 项目的设置文件中，
将 corsheaders 添加到 INSTALLED_APPS 中，
并将 'corsheaders.middleware.CorsMiddleware' 添加到 MIDDLEWARE 列表的合适位置。
确保将 'corsheaders.middleware.CorsMiddleware' 放在其他中间件的前面，以确保它能够正确处理跨域请求。

# 允许所有的跨域请求
CORS_ORIGIN_ALLOW_ALL = True
# 允许指定的域名进行跨域请求
CORS_ORIGIN_WHITELIST = [
  'http://example.com',
  'https://example.com',
]

重启 Django 服务器

```


## 配置 djangorestframework
```
pip3 install djangorestframework

在setting.py   INSTALLED_APPS内 注册
rest_framework

在下面添加   使用 自定义分页的  自定义异常  返回统一的格式
REST_FRAMEWORK = {
    # 分页
    'DEFAULT_PAGINATION_CLASS': 'utils.common_pagination.pagination_handler',
    # 异常
    'EXCEPTION_HANDLER': 'utils.common_exceptions.exception_handler',
}

```


## 配置脚本 文件 py_run.sh
```
./py_run.sh   启动虚拟环境运行django项目
./py_run.sh pip 依赖名称    
./py_run.sh d 关闭虚拟环境


#!/bin/bash

# 检查操作系统类型和处理器架构
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac 环境
    COMMAND_SH_RUN="cd django/pvenv/bin/ && source activate && cd .. && cd .. && cd djangoproject && python3 manage.py runserver"
    COMMAND_SH_PIP="cd django/pvenv/bin/ && source activate && pip3 install $2"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    # Windows 环境
    COMMAND_SH_RUN='cd django/pvenv/bin/activate.bat && cd .. && cd .. && cd djangoproject && python3 manage.py runserver'
else
    echo "Unsupported operating system."
    exit 1
fi

# 检查命令行参数
if [ "$1" = "pip" ]; then
    # 停用虚拟环境
    echo "--------------------------------"
    eval $COMMAND_SH_PIP
else
    # 启动服务器
    echo "==============================="
    eval $COMMAND_SH_RUN
fi
```







