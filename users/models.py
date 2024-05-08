from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
# 模型层，用来创建 数据库的 表模型


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=32, unique=True)
    # 添加其他字段

    def __str__(self):
        return self.username



