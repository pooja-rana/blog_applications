from django.contrib import admin
from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', "email", "name", "password", "bio", "picture", "phone_number")
    list_filter = ('id', 'name')
    search_fields = ('id',)
