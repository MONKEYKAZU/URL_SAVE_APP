from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path('register', views.AccountRegistration.as_view(), name='createacount'),
    path("logout",views.Logout,name="Logout"),
    path("home",views.home,name="home"),
    path("create",views.URLsave.as_view(),name="create"),
    path("rand",views.Randomviews.as_view(),name="rand"),
]

