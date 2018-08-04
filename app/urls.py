from django.conf.urls import url
from django.contrib.auth import login,logout
from app import views
from django.urls import path, include, re_path
from .views import fornecedor_new
from .views import fornecedor_update



urlpatterns = [
    path('', views.home, name='app'),
    path('delete/<int:id>/', views.fornecedor_delete, name='fornecedor_delete'),
    path('new/', fornecedor_new, name="fornecedor_new"),
    path('update/<int:id>/', fornecedor_update, name="fornecedor_update"),

] 