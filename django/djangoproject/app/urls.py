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
from django.urls import path
from app.views.common import LoginView, UserInfoView, UpdataView, UpdataPassView
# 角色
from app.views.roles import RoleInsertView, RoleListView, RoleDeleteView, RoleUpdataView, RoleDetailView
# 用户
from app.views.users import UserInsertView, UserDeleteView, UserUpdataView, UserListView, UserDetailView
# 通知
from app.views.notices import NoticeInsertView, NoticeDeleteView, NoticeUpdataView, NoticeListView, NoticeDetailView



urlpatterns = [
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('userInfo', UserInfoView.as_view(), name='userInfo'), # 获取个人信息
    path('updata', UpdataView.as_view(), name='updata'), # 修改个人信息
    path('updata/pass', UpdataPassView.as_view(), name='updataPass'), # 修改个人信息
    


    # 角色相关
    path('role/insert', RoleInsertView.as_view(), name='RoleInsert'), # 新增
    path('role/delete', RoleDeleteView.as_view(), name='RoelDelete'), # 删除
    path('role/updata', RoleUpdataView.as_view(), name='RoelUpdata'), # 编辑
    path('role/list', RoleListView.as_view(), name='RoelList'), # 获取列表
    path('role/detail', RoleDetailView.as_view(), name='RoelDetail'), # 获取详情

    # 账号相关
    path('user/insert', UserInsertView.as_view(), name='UserInsert'), # 新增
    path('user/delete', UserDeleteView.as_view(), name='UserDelete'), # 删除
    path('user/updata', UserUpdataView.as_view(), name='UserUpdata'), # 编辑
    path('user/list', UserListView.as_view(), name='UserList'), # 获取列表
    path('user/detail', UserDetailView.as_view(), name='UserDetail'), # 获取详情

    # 通知相关
    path('notice/insert', NoticeInsertView.as_view(), name='NoticeInsert'), # 新增
    path('notice/delete', NoticeDeleteView.as_view(), name='NoticeDelete'), # 删除
    path('notice/updata', NoticeUpdataView.as_view(), name='NoticeUpdata'), # 编辑
    path('notice/list', NoticeListView.as_view(), name='NoticeList'), # 获取列表
    path('notice/detail', NoticeDetailView.as_view(), name='NoticeDetail'), # 获取详情
]


