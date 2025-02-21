from django.urls import path, include

from rest_framework.routers import DefaultRouter

from blog_management.views import BlogViewSet, CommentViewSet

app_name = "blog_management"

router = DefaultRouter()

router.register("blogs", BlogViewSet, basename="blog")
router.register("comment", CommentViewSet, basename="comment")


urlpatterns = [
    path('', include(router.urls))
    ]
