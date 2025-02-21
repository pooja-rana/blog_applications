from django.apps import AppConfig


class BlogManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_management'

    def ready(self):
        import blog_management.signals
