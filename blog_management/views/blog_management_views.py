from http.client import responses

from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from blog_management.message import BlogMessages
from core.models import Blog
from core.response import ResponseHandler
from core.custome_pagination import ListingPaginator
from blog_management.services import AddBlogService, UpdateBlogService
from blog_management.serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    """ This blog viewset is used for the blog add , delete, edit, list"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author__name", "category", "tags__name", "status"]
    search_fields = ["title", "content", "status", "author__name", "category", "tags__name"]
    ordering_fields = ["publication_date"]
    pagination_class = ListingPaginator
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def create(self, request):
        """ create method for the publish blog"""
        payload = AddBlogService().execute(request)
        return ResponseHandler.success(message=BlogMessages.ENTITY_ADDED_SUCCESSFULLY, payload=payload)

    def partial_update(self, request, pk=None):
        """ This is update method for blog update"""
        payload = UpdateBlogService().execute(request, pk)
        return ResponseHandler.success(message=BlogMessages.ENTITY_UPDATED_SUCCESSFULLY, payload=payload)

    def retrieve(self, request, pk):
        """ get blog details based on selected pk id """
        blog_detail = Blog.objects.get(id=pk)
        if not blog_detail:
            raise ValidationError({"message": BlogMessages.ENTITY_DOES_NOT_EXISTS})
        response = BlogSerializer(blog_detail, context={"view": self})
        return ResponseHandler.success(
            message=BlogMessages.ENTITY_DATA_SUCCESSFULLY_RETRIEVE,
            payload=response.data
        )


    def destroy(self, request, *args, **kwargs):
        """ This method is used for the delete own blog """
        instance = self.get_object()
        if instance.author != request.user:
            return ResponseHandler.bad_request(message=BlogMessages.YOU_CAN_ONLY_DELETE_YOUR_OWN_BLOGS)
        super().destroy(request, *args, **kwargs)
        return ResponseHandler.success(message=BlogMessages.BLOG_DELETED_SUCCESSFULLY)
