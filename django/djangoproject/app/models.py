
from django.db import models

# 基类：可以把通用的字段定义这里，其他地方继承基类即可拥有
class BaseModel(models.Model):

    isDelete = models.BooleanField(verbose_name='是否删除', default=False, null=True, blank=True, db_column='is_delete')
    createTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True, blank=True, db_column='create_time')
    updataTime = models.DateTimeField(verbose_name='修改时间', auto_now=True, null=True, blank=True, db_column='updata_time')

    class Meta:
        abstract = True


# 角色表
class Roles(BaseModel, models.Model):

    name = models.CharField(verbose_name="角色名称", max_length=32, blank=False)
    detail = models.TextField(verbose_name="角色说明", null=True, default="")
    permission = models.TextField(verbose_name="选中的权限")
    pathList = models.TextField(verbose_name="关于权限的所有路由", db_column="path_list")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户角色'
        db_table = 'roles'


# 用户表
class Users(BaseModel, models.Model):

    gender_choices = ((1, '男'), (2, '女'))

    type_choices = ((1, '内置'), (2, '创建'))

    phone = models.CharField(verbose_name='手机号&账号', max_length=11)
    passWord = models.CharField(verbose_name="密码", max_length=64, db_column="pass_word")
    passWordMd5 = models.CharField(verbose_name="加密密码", max_length=64, db_column="pass_word_md5")
    name = models.CharField(verbose_name="姓名", max_length=32, default="")
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices, null=True)
    age = models.IntegerField(verbose_name='年龄', null=True)
    region = models.CharField(verbose_name='省市区', max_length=64, default="")
    address = models.CharField(verbose_name='详细地址', max_length=64, default="")
    type = models.IntegerField(verbose_name='用户类型', choices=type_choices, default=2)
    roleId = models.ForeignKey(Roles, verbose_name='用户角色', on_delete=models.CASCADE, null=True, blank=True, db_column='role_id')
    is_active = models.BooleanField(verbose_name='是否激活', default=True)
    detail = models.TextField(verbose_name="账号说明", null=True, default="")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = '用户'
        db_table = 'users'



# 通知表
class Notices(BaseModel, models.Model):
    
    title = models.CharField(verbose_name='通知标题', max_length=32)
    detail = models.TextField(verbose_name='通知详情', null=True, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '通知'
        db_table = 'notices'




