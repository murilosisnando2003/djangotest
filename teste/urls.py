from django.conf.urls import url
from django.contrib.auth.views import login, logout
from teste import views
from django.urls import path, include, re_path



urlpatterns = [
    path('', views.home, name='teste'),

] 