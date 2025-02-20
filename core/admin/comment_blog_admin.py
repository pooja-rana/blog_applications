from django.contrib import admin

from core.models import Comment


@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", )
    list_filter = ("id", "user__name", "text", "created_at")
    search_fields = ("id",)
