from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .tags_serializer import TagSerializer
from core.constant import CategoryConst, BlogStatusConst
from core.models import Blog, Tag
from blog_management.message import BlogMessages


class BlogSerializer(serializers.ModelSerializer):
    """ This serializer is used for the blog details add"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context and (self.context['view'].action in ('list', 'retrieve')):
            self.fields['tags'] = TagSerializer(many=True)
            self.fields['author'] = serializers.CharField(source='author.name')

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
        input_formats="%d-%m-%Y %H:%M",
        required=True,
        allow_null=True,
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    content=serializers.CharField(required=False, allow_null=True)
    category = serializers.ChoiceField(
        required=True,
        choices=CategoryConst.choices(),
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    status = serializers.ChoiceField(
        choices=BlogStatusConst.choices(),
        required=True,
        error_messages={
            "required": BlogMessages.ENTITY_REQUIRED_FIELD,
        }
    )

    class Meta:
        model = Blog
        fields = ("id", "title", "publication_date", "content", "category", "tags", "author", "status")
