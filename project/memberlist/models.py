from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    phoneNumber = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100, default = 'none')

    def get_full_name(self):
        # 사용자의 전체 이름 반환
        return f"{self.first_name} {self.last_name}"