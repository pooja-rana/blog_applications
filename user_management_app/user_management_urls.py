from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user_management_app.views import UserDetailRegisterView, UserLoginView, UserProfileUpdateView

app_name = "user_management_app"

router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path("register-detail/", UserDetailRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile-update/", UserProfileUpdateView.as_view(), name="profile"),
    ]
