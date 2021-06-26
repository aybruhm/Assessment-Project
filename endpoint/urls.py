from django.urls import path
from endpoint import views

app_name = "endpoint"

urlpatterns = [
    path("", views._home, name="home"),
    path("register/", views._register, name="register"),
    path("login/", views._login, name="login"),
    path("logout/", views._logout, name="logout")
]
