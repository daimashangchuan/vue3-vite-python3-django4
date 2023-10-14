
from rest_framework import serializers

from app.models import Notices

from app.error.error import NoticeError

# 创建 & 编辑   用作保存数据
class NoticesSerializers(serializers.Serializer):

    title = serializers.CharField(max_length=32, required=True)
    detail = serializers.CharField(allow_null=True, allow_blank=True)

    def validate_title(self, value):
        
        # 获取当前角色实例
        instance = getattr(self, "instance", None)
        if instance and instance.title == value:
            return value

        if Notices.objects.filter(title=value, isDelete=False).exists():
            raise serializers.ValidationError(NoticeError.MSG_1200)
        
        return value
    
    def create(self, validated_data):
        # 根据validated_data中的数据创建一个新的Roles对象
        role = Notices.objects.create(**validated_data)
        return role

    def update(self, instance, validated_data):
        if instance.isDelete:
            raise serializers.ValidationError(NoticeError.MSG_1300)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

# 查询数据
class NoticesModelSerializers(serializers.ModelSerializer):
    
    class Meta():
        model = Notices
        # fields = '__all__'
        exclude = ['isDelete']



