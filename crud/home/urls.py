from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.welcome),
    path("home",views.home),
    path("login",views.login),
    path("table",views.table),
    path("base",views.base),
]