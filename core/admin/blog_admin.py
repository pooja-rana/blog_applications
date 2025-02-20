from django.contrib import admin
from core.models import Blog, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", )
    list_filter = ("id", "title", "publication_date", "author", "content", "category", "tags", "status",)
    search_fields = ("id",)



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", )
    list_filter = ("id", "name",)
    search_fields = ("id",)
