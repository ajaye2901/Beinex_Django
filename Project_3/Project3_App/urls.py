from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('cart/',ViewCart,name='cart'),
    path('login/',user_login,name = 'login'),
    path('logout/',user_logout)
]