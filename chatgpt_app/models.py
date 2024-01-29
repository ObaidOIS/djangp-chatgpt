# chatgpt_app/models.py

from django.contrib.auth.models import User
from django.db import models


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_message = models.TextField()
    chatgpt_response = models.TextField()
