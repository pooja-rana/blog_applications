from rest_framework import serializers

from core.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """This serializer is used for the comment add"""
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "blog", "text", "parent", "up_votes", "down_votes", "created_at", "replies"]
        read_only_fields = ["up_votes", "down_votes"]

    def get_replies(self, obj):
        """Recursively fetch nested replies."""
        return CommentSerializer(obj.replies.all(), many=True).data
