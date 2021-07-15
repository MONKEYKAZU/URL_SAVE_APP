from env1 import urls
from django import views
from myapp.models import Urls_save
from .forms import AccountForm,URL_SAVEForm
from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView #テンプレートタグ
from django.views.generic.edit import FormView #フォームタグ
# from django.contrib.auth.mixins import LoginRequiredMixin
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#indexhtmlにuserを返す
@login_required
def home(request):
    url = Urls_save.objects.filter(user = request.user)
    # url = Urls_save.objects.all()
    print(url)
    params = {
        "UserID":request.user,
        "url_view":url
        }
    return render(request, "index.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        self.params["Accounterror"] = False
        return render(request,"createacount.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # アカウント作成情報更新

            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)
            self.params["AccountCreate"] = False
            self.params["Accounterror"] = True

        return render(request,"createacount.html",context=self.params)

#urlを新規で保存する
class URLsave(FormView):
    # def __init__(self):
    #     self.params = {
    #     "url_form": URL_SAVEForm(),
    #     }

    form_class = URL_SAVEForm
    template_name = 'url_save.html'

    #getは絶対いる
    def get(self,request):
        self.params = {"UserID":self.request.user}
        self.params["url_form"] = URL_SAVEForm()
        print(self.request.user)
        return render(request,"url_save.html",context=self.params)


    # フォームの値が正しいかどうかの検証をして　検証が通ったら実行される部分だよ
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.user=self.request.user
        qryset.save()
        print(qryset)
        return HttpResponseRedirect(reverse('home'))

    # #このhtmlを表示する時に、少なくとも一回はgetするから絶対必要
    # #というよりgetとpostはセットと覚えた方がよさそう
    # def get(self,request):
    #     self.params = {"UserID":self.request.user}
    #     self.params["url_form"] = URL_SAVEForm()
    #     print(self.request.user)
    #     return render(request,"url_save.html",context=self.params)


    #Post処理
    # def post(self,request):
    #     self.params["url_form"] = URL_SAVEForm(data=request.POST)

    #     #フォーム入力の有効検証
    #     if self.params["url_form"].is_valid():
    #         # アカウント情報をDB保存
    #         urls_parm = self.params["url_form"].save()
    #         urls_parm.user = self.request.user
    #         # パスワードをハッシュ化
    #         # urls_parm.set_user(Urls_save.user)
    #         # ハッシュ化パスワード更新
    #         urls_parm.save()
    #         print(urls_parm)

    #     else:
    #         # フォームが有効でない場合
    #         print(self.params["url_form"].errors)

    #     return render(request,"url_save.html",context=self.params)