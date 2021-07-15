from django.db import models
#ユーザー認証
from django.contrib.auth.models import User

#ユーザーアカウントのモデルクラス
# class Account(models.Model):

    
#     #ユーザー認証のインスタンス(1vs1関係)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # url = models.URLField()
#     # tag1 = models.CharField(max_length=50)
#     # tag2 = models.CharField(max_length=50)
#     # tag3 = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user.username

class Urls_save(models.Model):

    user = models.ForeignKey(User,unique=False,on_delete=models.CASCADE)
    url = models.TextField()
    tag1 = models.CharField(max_length=50)
    tag2 = models.CharField(max_length=50)
    tag3 = models.CharField(max_length=50)
    
    #ここの部分でadminで表示する部分を返す。
    def __str__(self):
        return self.url