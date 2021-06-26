from django.urls import path
from endpoint import views

urlpatterns = [
    path("register/", views._register, name="register"),
    path("login/", views._login, name="login"),
    path("logout/", views._logout, name="logout")
]
