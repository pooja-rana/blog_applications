from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from core.response import ResponseHandler
from user_management_app.messages import UserDetailsMessages
from user_management_app.serializers import UserDetailUpdateSerializer
from user_management_app.services import UserProfileUpdateService


class UserProfileUpdateView(RetrieveUpdateAPIView):
    """API for users to update their own profile"""
    serializer_class = UserDetailUpdateSerializer
    permission_classes = [IsAuthenticated]


    def patch(self, request, *args, **kwargs):
        payload= UserProfileUpdateService().execute(request)
        return ResponseHandler.success(
            message=UserDetailsMessages.PROFILE_UPDATE_SUCCESSFULLY,
            payload=payload
        )
