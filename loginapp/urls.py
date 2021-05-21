from django import contrib, urls
from django.contrib import auth
from django.urls import include, path
from . import views as loginviews

urlpatterns = [
    path("", loginviews.home, name="home"),
    path("home/", loginviews.home, name="home"),
    path("register/", loginviews.register, name="register"),
    path("", include("django.contrib.auth.urls")),
]
