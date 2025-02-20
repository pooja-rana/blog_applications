from django.urls import path, include

from rest_framework.routers import DefaultRouter

from blog_management.views import BlogViewSet

app_name = "blog_management"

router = DefaultRouter()

router.register("blogs", BlogViewSet, basename="blog")


urlpatterns = [
    path('', include(router.urls))
    ]
