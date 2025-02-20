from rest_framework.exceptions import ValidationError
from blog_management.serializers import BlogSerializer

class AddBlogService:

    def execute(self, request):
        """This is main method to publish blog."""
        serializer = BlogSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save(author=request.user)
        return serializer.data
