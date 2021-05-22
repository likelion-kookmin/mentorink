from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(AbstractUser):
    USER_POS = (
        ('전문가', '전문가'),
        ('일반', '일반'),
    )
    nickname = models.CharField(max_length=100)
    position = models.CharField(
        max_length=10, choices=USER_POS, help_text='전문가인지 일반유저인지 선택해주세요!')
