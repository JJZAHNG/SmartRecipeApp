# users/serializers.py
from rest_framework import serializers
from .models import CustomUser
# from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser # 校验表模型
        fields = ['id', 'username', 'email', 'phone_number', 'password'] # 校验字段
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data): # 创建用户的方法，并把用户写进数据库
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


