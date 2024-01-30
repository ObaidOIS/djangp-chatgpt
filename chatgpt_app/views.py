from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .ChatGPTService import ChatGPTService
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .models import Conversation
from django.contrib.auth import authenticate
from .decorators import jwt_authentication_required
from .serializer import ConversationSerializer


@api_view(["POST"])
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


@api_view(["POST"])
@jwt_authentication_required
def chat(request):
    message = request.data.get("message")
    response = ChatGPTService.send_request(message)  # Call your ChatGPT service
    user = request.user  # Get the user instance directly
    serilized_data = ConversationSerializer(
        data={"user": user.id, "user_message": message, "chatgpt_response": response}
    )
    if serilized_data.is_valid():
        serilized_data.save()
        return Response({"message": message, "response": response})
    else:
        return Response({"error": serilized_data.errors}, status=400)


@api_view(["GET"])
@jwt_authentication_required
def getChat(request):
    conversations = Conversation.objects.filter(user=request.user)
    conversations = ConversationSerializer(conversations, many=True).data
    return Response({"conversations": conversations})
