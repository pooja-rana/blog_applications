from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView

from core.models import User
from core.response import ResponseHandler
from user_management_app.serializers import UserRegisterSerializer

from user_management_app.messages import UserDetailsMessages


class UserDetailRegisterView(CreateAPIView):
    """ User register details"""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


    def create(self, request, *args, **kwargs):
        """save details of register user"""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return ResponseHandler.success(message=UserDetailsMessages.USER_REGISTER_SUCCESSFULLY, payload=serializer.data)
