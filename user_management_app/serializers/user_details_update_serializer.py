from rest_framework import serializers

from core.models import User
from .user_register_serializer import UserRegisterSerializer


class UserDetailUpdateSerializer(UserRegisterSerializer):
    """user profile update serializer"""

    class Meta:
        model = User
        fields = ("id", "name", "bio", "picture", "phone_number")
