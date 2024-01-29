# chatgpt_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .ChatGPTService import ChatGPTService  # Import your ChatGPT service
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from .models import Conversation
import requests
from django.contrib.auth import authenticate


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "Both username and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({"access_token": access_token}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


# @permission_classes([AllowAny])
permission_classes = [IsAuthenticated]


class ChatView(APIView):
    def post(self, request):
        message = request.data.get("message")
        print(message)
        response = ChatGPTService.send_request(message)  # Call your ChatGPT service
        Conversation.objects.create(
            user=request.user, message=message, response=response
        )
        return Response({"message": message, "response": response})

    def get(self, request):
        conversations = Conversation.objects.filter(user=request.user)
        return Response({"conversations": conversations})
