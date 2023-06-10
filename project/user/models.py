from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phoneNum = models.CharField(max_length=20)              # 핸드폰번호

