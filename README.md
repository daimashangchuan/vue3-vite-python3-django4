# 项目说明
```
git clone https://gitlab.com/sunjiwei1/vue3-vite-python3-django4.git

cd vue_vite_ts && npm install || yarn

cd django   减压  pvenv

```

## 前端环境
```
"@element-plus/icons-vue": "^2.1.0",
"@types/js-cookie": "^3.0.3",
"axios": "^1.4.0",
"dayjs": "^1.11.8",
"element-plus": "^2.3.6",
"js-cookie": "^3.0.5",
"normalize.css": "^8.0.1",
"pinia": "^2.1.3",
"pinia-plugin-persistedstate": "^3.1.0",
"qs": "^6.11.2",
"sass": "^1.62.1",
"ts-md5": "^1.3.1",
"vue": "^3.2.47",
"vue-router": "^4.2.2"
"@vitejs/plugin-vue": "^4.1.0",
"typescript": "^5.0.2",
"unplugin-auto-import": "^0.16.4",
"unplugin-vue-components": "^0.25.0",
"vite": "^4.3.9",
```



## 后端环境
```
python              3.11.0
pip                 23.0.1
Django              4.2.2
django-cors-headers 4.0.0
djangorestframework 3.14.0
pyjwt               2.7.0
PyMySQL             1.0.3
```


##  目录说明
```
django              用到的是python的一个web框架的，python后端项目

vue_vite_ts         vue3 + vue-router4 + ts + vite4 + element-plus2  搭建的后台管理

.gitignore          git 忽略文件

api.md              接口文档 

mysql.md            学习 mysql 的一些基础用法

process.md          搭建django，配置django依赖的学习过程
```



##  django目录说明
```
使用创建django项目  django django-admin startproject 项目名

djangoproject 文件
     djangoproject 文件
        __init__.py    
        asgi.py   存储asgi设定的文件的文件，用于存储asgi设定的文件。如果使用ASGI部署django，一般情况下不需要更改
        wsgi.py   存储wsgi设定的文件的文件，用于存储wsgi设定的文件。如果使用WSGI部署django，一般情况下不需要更改
        setting.py    项目的配置文件
        urls.py       项目的路由文件
    manage.py  运行文件

    app 文件     
      使用 python3 manage.py startapp app名称 创建 初始的文件目录
          migrations      迁移记录  不用需改  自动生成
            __init.py__  
          admin.py        内部管理后台的配置（不用）
          apps.py         不用修改
          models.py       数据库，类->sql语句（ORM） py类转化为sql语句
          tests.py        单元测试
          views.py        视图函数

      改造之后
          error 新建错误文件  用来返回给前端的错误提示文案和状态
              error.py  错误状态和文案

          management => commands    management/commands目录用于存储自定义的管理命令
              init_user.py 初始化登录数据

          middlewares  用来存放自定义中间件
              auth_token_middlewares.py

          migrations      迁移记录  不用需改  自动生成
          
          serializer   配置的序列化文件（读出库的内容前端是渲染不了的所以需要序列化） 对数据库做 增/删/改/查的时候对数据做校验
              NoticesSerializers.py   通知模块的序列化
              RolesSerializers.py     角色模块的序列化
              UsersSerializers.py     用户模块的序列化

          view 新建视图文件  删除了view.py文件

          admin.py        内部管理后台的配置（不用）

          apps.py         不用修改

          models.py       数据库，类->sql语句（ORM） py类转化为sql语句

          tests.py        单元测试

          urls.py         新建用做管理app这个web路由与其他新建的  python3 manage.py startapp app名称 路由隔离
    
    utils  新建 用来存放自定义方法
        common_exceptions.py  django带有的报错，有一些是捕获不到的   需要自定义查找是哪里报错。
        common_logger.py     用来打印日志   直接用 print 也可以
        common_response.py    自定义响应的方法  主要是 统一返回格式
        common_pagination.py    使用 django 自定的分页功能  自定义参数名，最大，最小条数
```


##  python的 环境配置与项目搭建（mac）
### 下载 python3
```
mac 自带的是 python2 版本  
一：使用  brew 安装
1：brew search python3   查询所有可以安装的 python3 的版本
2：brew install python || brew install python@3.11   安装最新版本或者 项目需要的python3的版本



二：查看版本
python --version  显示还是 Python 2.7.18  （mac自带的版本）
python3 --version   报错  zsh: command not found: python3  需要配置环境变量



三：需要配置环境变量 
Apple芯片  sudo vim ~/.zshrc  sudo最高权限  打开.zshrc文件  
Intel芯片  sudo vim ~/.bash_profile  sudo最高权限  打开.bash_profile文件  

辅助：如果两个配置文件不存在，可以手动创建
cd ~
touch .zshrc
vim .zshrc
辅助：如果不想走命令行的方式修改环境变量，也可以直接打开文件进行可视化修改，不支持 Linux 可视化
open ~/.zshrc

配置环境  找到安装 python@3.11 的目录   
可以在终端 which python  或者 ps -ef|grep python3   搜索本地路径
# python STSRT
export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"
# python END

在终端界面下输入以下命令，让配置文件的修改生效，并查看环境变量是否设置成功
source ~/.bash_profile 
echo $PATH

python3 --version   Python 3.11.3 没有问题了

```

### 安装数据库 mysql（本人数据库 mysql  Ver 8.0.32 for macos13 on arm64 (MySQL Community Server - GPL)）
```

https://dev.mysql.com/downloads/mysql/   官网
配置数据库账号   
账号名/密码：  python/123456    
数据库：python

创建数据库
CREATE DATABASE python  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
设置权限
GRANT ALL PRIVILEGES ON python.*  TO 'python'@'hostname';
```




## 运行项目
### 运行后端项目
```
修改 setting.py ( django/djangoproject/djangoproject/settings.py )
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

运行 
启动 venv 虚拟环境  回到根目录  启动django项目   
cd django/pvenv/bin/ && source activate && cd .. && cd .. && cd djangoproject && python3 manage.py runserver
也可以运行脚本
mac 需要添加权限 chmod +x py_run.sh
启动： ./py_run.sh   
停止：./py_run.sh d

创建数据库的表（创建一次就可以，之后有修改 models.py 文件 重新运行 ）
python3 manage.py makemigrations
python3 manage.py migrate

创建项目登录密码
可以修改 init_user.py 文件中的 phone 和 password  
用命令创建的账号密码  type为1  拥有所有的权限
python3 manage.py init_user


启动 ajango 项目
cd django/djangoproject/
python3 manage.py runserver

```



### 运行前端项目
```
cd vue_vite_ts
npm install || yarn
npm start || yarn start

浏览器打来 http://localhost:9686/#/



```






