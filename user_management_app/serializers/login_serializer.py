from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from user_management_app.messages import UserDetailsMessages


class UserLoginSerializer(TokenObtainPairSerializer):
    """ User login validate serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError(
                {
                    "messages": UserDetailsMessages.USERNAME_PASSWORD_NOT_MATCH,
                    "status": False
                })

        refresh = RefreshToken.for_user(user)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
            },
        }
