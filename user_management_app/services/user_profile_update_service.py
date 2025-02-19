from django.utils.regex_helper import normalize
from rest_framework.exceptions import ValidationError

from core.models import User
from user_management_app.messages import UserDetailsMessages
from user_management_app.serializers import UserDetailUpdateSerializer


class UserProfileUpdateService:

    def execute(self, request):
        """ main method for user profile update"""
        user = User.objects.get(id=request.user.id)
        if not user:
            raise ValidationError(UserDetailsMessages.USER_UPDATE_ONLY_OWN_PROFILE)
        serializer = UserDetailUpdateSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.error)
        serializer.save()
        return serializer.data
