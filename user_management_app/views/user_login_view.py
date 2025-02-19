from rest_framework_simplejwt.views import TokenObtainPairView

from core.response import ResponseHandler
from user_management_app.serializers import UserLoginSerializer
from user_management_app.messages import UserDetailsMessages


class UserLoginView(TokenObtainPairView):
    """ This serializer is used for login"""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        """ user login api"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return ResponseHandler.success(
            message=UserDetailsMessages.USER_LOGIN_SUCCESSFULLY,
            payload=serializer.validated_data
        )
