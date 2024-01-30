from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import TokenError, AccessToken
from django.contrib.auth.models import User


def jwt_authentication_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        authorization_header = request.headers.get("Authorization")

        if not authorization_header or not authorization_header.startswith("Bearer "):
            return Response(
                {"error": "Authorization header with Bearer token is required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token = authorization_header.split(" ")[1]

        try:
            access_token = AccessToken(token)
            user = access_token.payload.get("user_id")
            request.user = User.objects.get(pk=user)
        except TokenError:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        return view_func(request, *args, **kwargs)

    return _wrapped_view
