from django.urls import path, include, re_path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('register', views.app_register, name='register'),
    path('login', views.app_login, name='login'),
    path('logout', views.app_logout, name='logout'),
]
