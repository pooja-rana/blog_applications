from celery import shared_task
from django.core.mail import send_mail

from core.models import Blog


@shared_task
def send_blog_published_email(blog_id):
    """Send an email when a blog is published."""
    blog = Blog.objects.get(id=blog_id)

    subject = f"New Blog Published: {blog.title}"
    message = f"Check out our latest blog: {blog.title}\n\n{blog.content}"

    send_mail(subject, message)
