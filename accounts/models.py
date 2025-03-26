from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# login modeling
class User(AbstractUser): 
    pass
    #phone = models.CharField(max_length=100) 기본에서 추가하고 싶은 기능