from django.db import models
from accounts.models import User
from django.conf import settings # 2
from django.contrib.auth import get_user_model # 3

# Create your models here.

# 게시글 모델
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 1. 직접 참조 
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # accounts와 연결하도록 경로 설정

    # 2. setting.py 변수 활용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    
    # 3. get_user_model
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# 댓글 모델
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 1:N
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 1:N
