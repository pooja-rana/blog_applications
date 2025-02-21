from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Blog
from core.constant import BlogStatusConst
from .tasks import send_blog_published_email

@receiver(post_save, sender=Blog)
def blog_published_signal(sender, instance, created, **kwargs):
    """
    Triggered when a blog is updated or created.
    If the blog status is changed to 'published', send an email using Celery.
    """
    if instance.status == BlogStatusConst.PUBLISHED.value:
        send_blog_published_email.delay(instance.id)
