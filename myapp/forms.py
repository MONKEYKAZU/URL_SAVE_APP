from .models import Urls_save
from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.forms import fields
# from .models import Account

#フォームクラス作成
class AccountForm(forms.ModelForm):
    """
    アカウント作成のフォーム作成
    """
    #パスワード入力：非表示対応
    #ここでplaceholder名を指定
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'}))

    class Meta():
        #ユーザー認証
        model = User
        #フィールド指定
        fields = ('username','email','password')
        #placeholder名を指定
        widgets = {
            'username'   : forms.TextInput(attrs={'placeholder': 'ユーザーID'}),
            'email'    :  forms.TextInput(attrs={'placeholder': 'e-mail'}),
        }
        

class URL_SAVEForm(forms.ModelForm):
    """
    URLを保存する為のフォーム
    """
    title = forms.CharField(max_length=50)
    url = forms.URLField()
    tag1 = forms.CharField(max_length=50,required=False)
    tag2 = forms.CharField(max_length=50,required=False)
    tag3 = forms.CharField(max_length=50,required=False)

    class Meta():
        model = Urls_save

        fields = ('title','url','tag1','tag2','tag3')

class RANDOMForm(forms.Form):
    """
    乱数作成のフォーム
    """
    ransu = forms.IntegerField()

    fieids = ('ransu')