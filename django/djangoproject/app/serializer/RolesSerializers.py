
from rest_framework import serializers

from app.models import Roles

from app.error.error import RoleError

# 创建 & 编辑   用作保存数据
class RolesSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=32, required=True)
    detail = serializers.CharField(allow_null=True, allow_blank=True)
    permission = serializers.CharField(required=True)
    pathList = serializers.CharField(required=True)

    def validate_name(self, value):
        # 获取当前角色实例
        instance = getattr(self, "instance", None)
        if instance and instance.name == value:
            return value
        
        if Roles.objects.filter(name=value, isDelete=False).exists():
            raise serializers.ValidationError(RoleError.MSG_1200)
        return value
    
    def create(self, validated_data):
        # 根据validated_data中的数据创建一个新的Roles对象
        role = Roles.objects.create(**validated_data)
        return role

    def update(self, instance, validated_data):
        if instance.isDelete:
            raise serializers.ValidationError(RoleError.MSG_1300)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

# 查询数据
class RolesModelSerializers(serializers.ModelSerializer):

    class Meta():
        model = Roles
        # fields = '__all__'
        exclude = ['isDelete']

