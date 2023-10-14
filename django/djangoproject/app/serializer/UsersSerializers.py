
from rest_framework import serializers
from app.models import Users, Roles
from app.serializer.RolesSerializers import RolesModelSerializers
from app.error.error import UserError


# 创建 & 编辑
class UsersSerializers(serializers.Serializer):

    phone = serializers.CharField(max_length=11, required=True)
    passWord = serializers.CharField(max_length=64, required=True)
    passWordMd5 = serializers.CharField(max_length=64, required=True)
    name = serializers.CharField(max_length=32, required=True)
    gender = serializers.IntegerField(allow_null=True)
    age = serializers.IntegerField(allow_null=True)
    region = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
    address = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
    type = serializers.IntegerField(allow_null=True, default=2)
    roleId = serializers.PrimaryKeyRelatedField(queryset=Roles.objects.all(), allow_null=True, required=True)
    detail = serializers.CharField(allow_null=True, allow_blank=True)

    def validate_phone(self, value):
        # 获取实例
        instance = getattr(self, "instance", None)

        # 编辑自己 phone 是可以重复的
        if instance and instance.phone == value:
            return value

        # 判断除了自己 phone在数据库中是否存在
        if Users.objects.filter(phone=value, isDelete=False).exists():
            raise serializers.ValidationError(UserError.MSG_1200)
 
        return value

    # 创建
    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    # 编辑
    def update(self, instance, validated_data):

        passWord = validated_data.pop('passWord', None)
        passWordMd5 = validated_data.pop('passWordMd5', None)
        # 修改密码
        if passWord:
            validated_data['passWord'] = passWord
        else:
            validated_data['passWord'] = instance.passWord
            
        if passWordMd5:
            validated_data['passWordMd5'] = passWordMd5
        else:
            validated_data['passWordMd5'] = instance.passWordMd5

        if instance.isDelete:
            raise serializers.ValidationError(UserError.MSG_1300)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()   
        return instance


# 查询数据
class UsersModelSerializers(serializers.ModelSerializer):

    role = RolesModelSerializers(source='roleId')
    class Meta():
        model = Users
        # fields = '__all__'
        exclude = ['passWord', 'isDelete', 'passWordMd5']







