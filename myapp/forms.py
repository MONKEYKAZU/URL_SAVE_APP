from .models import Urls_save
from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.forms import fields
# from .models import Account

#フォームクラス作成
class AccountForm(forms.ModelForm):
    #パスワード入力：非表示対応
    #ここでplaceholder指定
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'}))

    class Meta():
        #ユーザー認証
        model = User
        #フィールド指定
        fields = ('username','email','password')
        #プレースフォルダー名指定
        widgets = {
            'username'   : forms.TextInput(attrs={'placeholder': 'ユーザーID'}),
            'email'    :  forms.TextInput(attrs={'placeholder': 'e-mail'}),
        }
        

class URL_SAVEForm(forms.ModelForm):
    url = forms.URLField()
    tag1 = forms.CharField(max_length=50)
    tag2 = forms.CharField(max_length=50)
    tag3 = forms.CharField(max_length=50)

    class Meta():
        model = Urls_save

        fields = ('url','tag1','tag2','tag3')

        
