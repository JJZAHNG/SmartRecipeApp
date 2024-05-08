# users/views.py
# 视图层，用来接收前端穿过来的数据 并进行处理 的逻辑层
from rest_framework import generics # 自带的视图层演变成路由的一个工具
from .models import CustomUser
from .serializers import UserSerializer # 序列化器 有序列化 还有反序列化
from django.contrib.auth import authenticate # 认证结构
from rest_framework.authtoken.models import Token # Token 令牌 识别
from rest_framework.response import Response # 响应 code 200 msg:登录成功 code:401 402 msg;用户名错误，密码错误，手机号格式不对
from rest_framework import status 

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all() # 查询集
    serializer_class = UserSerializer # 序列化类

class UserLogin(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        print("校验：", username, password)
        user = authenticate(username=username, password=password)
        user = (username, password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

