from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.constant import CategoryConst, BlogStatusConst
from core.models import Blog, Tag
from blog_management.message import BlogMessages
from .comment_serializer import CommentSerializer
from .tags_serializer import TagSerializer


class BlogSerializer(serializers.ModelSerializer):
    """ This serializer is used for the blog details add"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context and (self.context['view'].action in ('list', 'retrieve')):
            self.fields['tags'] = TagSerializer(many=True)
            self.fields['author'] = serializers.CharField(source='author.name')
            self.fields['comments'] = serializers.SerializerMethodField()

    title = serializers.CharField(
        required=True,
        max_length=64,
        validators=[
            UniqueValidator(
                queryset=Blog.objects.all(),
                message=BlogMessages.ENTITY_ALREADY_EXISTS)
        ],
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
            "blank": BlogMessages.ENTITY_REQUIRED_FIELD,
            "max_length": BlogMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64),
        }
    )

    publication_date = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M",
        input_formats=["%d-%m-%Y %H:%M"],
        required=True,
        allow_null=True,
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    content=serializers.CharField(required=False, allow_null=True)
    category = serializers.ChoiceField(
        required=True,
        choices=CategoryConst.get_choices(),
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    status = serializers.ChoiceField(
        choices=BlogStatusConst.get_choices(),
        required=True,
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ("id", "title", "publication_date", "content", "category", "tags", "author", "status", "comments")

    def get_comments(self, obj):
        """Return only top-level comments (parent=None)."""
        top_level_comments = obj.comments.filter(parent__isnull=True)
        return CommentSerializer(top_level_comments, many=True).data if top_level_comments.exists() else []
