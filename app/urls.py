from django.conf.urls import url
from django.contrib.auth import login,logout
from app import views
from django.urls import path, include, re_path



urlpatterns = [
    path('', views.home, name='app'),
    path('delete/<int:id>/', views.fornecedor_delete, name='fornecedor_delete'),

] 