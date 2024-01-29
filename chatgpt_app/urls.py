# chatgpt_app/urls.py

from django.urls import path
from .views import ChatView, register_user, login_user

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("chat/", ChatView.as_view(), name="chatgpt-view"),
]
