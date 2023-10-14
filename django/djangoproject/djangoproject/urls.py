"""
djangoproject项目的URL配置。

“urlpatters”列表将URL路由到视图。有关更多信息,请参阅:
https://docs.djangoproject.com/en/4.2/topics/http/urls/

    示例:
    功能视图
    1.添加导入:从my_app导入视图
    2.将URL添加到URL模式:path('',views.home,name='home')

    基于类的视图
    1.添加导入:from other_app.views import主页
    2.将URL添加到URL模式:path('',Home.as_view(),name='Home')

    包括另一个URLconf
    1.导入include()函数:从django.url导入include,path
    2.将URL添加到URL模式:path('blog/',include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]
