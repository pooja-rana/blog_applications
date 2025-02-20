from rest_framework.exceptions import ValidationError

from blog_management.message import BlogMessages
from blog_management.serializers import BlogSerializer
from core.models import Blog


class UpdateBlogService:

    def execute(self, request, pk):
        """This is main method to update publish blog."""
        instance = Blog.objects.get(pk=pk)
        if not instance:
            raise ValidationError({"message":BlogMessages.ENTITY_DOES_NOT_EXISTS})
        if instance.author != request.user:
            raise ValidationError({"message":BlogMessages.YOU_CAN_ONLY_DELETE_YOUR_OWN_BLOGS})
        serializer = BlogSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return serializer.data
