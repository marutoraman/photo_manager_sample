from django.contrib import admin
from django.urls import path
from .views import signupfunc,loginfunc,menufunc,form

urlpatterns = [
    path('signup/',signupfunc,name='signup'),
    path('login/',loginfunc,name='login'),
    path('menu/',menufunc,name='menu'),
    path('form/',form,name='form'),
    # path('picture/',Picturefunc.as_view(), name ='picture'),
]