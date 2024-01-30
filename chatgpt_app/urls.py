from django.urls import path
from .views import chat, getChat, register_user, login_user

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("chat/", chat, name="chatgpt-view"),
    path("getChat/", getChat, name="getChat"),
]
