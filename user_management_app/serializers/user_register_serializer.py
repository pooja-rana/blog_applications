from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.constant import UserConst
from core.models import User
from user_management_app.messages import UserDetailsMessages


class UserRegisterSerializer(serializers.ModelSerializer):
    """ This is user detail serializer."""

    name = serializers.CharField(
        required=True,
        max_length=64,
        error_messages={
            "required": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
            "max_length": UserDetailsMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64)
        }
    )
    email = serializers.EmailField(
        required=True,
        max_length=64,
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message=UserDetailsMessages.EMAIL_ALREADY_EXISTS),
        ],
        error_messages={
            "invalid": UserDetailsMessages.INVALID_EMAIL,
            "required": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
            "blank": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
            "max_length": UserDetailsMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64)
        }
    )
    password = serializers.RegexField(
        write_only=True,
        required=True,
        max_length=64,
        regex=UserConst.PASSWORD_REGEX.value,
        error_messages={
            "invalid": UserDetailsMessages.INVALID_PASSWORD,
            "required": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
            "blank": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
            "max_length": UserDetailsMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64),
        })
    phone_number = serializers.RegexField(
        required=True,
        regex=UserConst.PHONE_NUMBER.value,
        allow_null=True,
        error_messages={
            "invalid": UserDetailsMessages.ENTITY_WITH_PHONE_NUMBER,
            "required": UserDetailsMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    bio = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ("id", "email", "name", "password", "bio", "picture", "phone_number")

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
