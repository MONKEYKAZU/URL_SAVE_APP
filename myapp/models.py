from django.db import models
#ユーザー認証
from django.contrib.auth.models import User


class Urls_save(models.Model):

    user = models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
    title = models.CharField(default=" ",max_length=50)
    url = models.TextField()
    tag1 = models.CharField(max_length=50)
    tag2 = models.CharField(max_length=50)
    tag3 = models.CharField(max_length=50)
    
    #ここの部分でadminで表示する部分を返す。
    def __str__(self):
        return self.title