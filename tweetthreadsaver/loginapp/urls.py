from django import contrib, urls
from django.contrib import auth
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("", include("django.contrib.auth.urls")),
]
