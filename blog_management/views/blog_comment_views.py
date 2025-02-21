from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from core.constant import BlogStatusConst
from core.models import Comment, Blog
from core.response import ResponseHandler
from blog_management.message import BlogMessages
from blog_management.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """ViewSet for managing comments on blogs, including voting and deletion."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Handles comment creation and ensures the blog is published."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = get_object_or_404(Blog, id=request.data.get("blog"), status=BlogStatusConst.PUBLISHED.value)
        serializer.save(author=request.user, blog=blog)
        return ResponseHandler.success(
            message=BlogMessages.COMMENT_ADDED_SUCCESSFULLY,
            payload=serializer.data
        )

    def partial_update(self, request, *args, **kwargs):
        """Handles up_voting or down_voting a comment."""
        comment = get_object_or_404(Comment, id=kwargs["pk"])
        vote_type = request.data.get("vote_type")

        if vote_type == "up_vote":
            comment.up_votes += 1
        elif vote_type == "down_vote":
            comment.down_votes += 1

        comment.save()
        return ResponseHandler.success(message=BlogMessages.VOTE_RECORDED,)

    def destroy(self, request, *args, **kwargs):
        """Allows only the blog author to delete any comment on their blog."""
        comment = get_object_or_404(Comment, id=kwargs["pk"])

        if request.user != comment.blog.author:
            return ResponseHandler.bad_request(message=BlogMessages.YOU_ARE_NOT_BLOG_OWNER)

        comment.delete()
        return ResponseHandler.success(message=BlogMessages.COMMENT_DELETED_SUCCESSFULLY)
