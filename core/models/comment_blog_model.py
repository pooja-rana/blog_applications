from django.db import models


class Comment(models.Model):
    """This is  the comment model that added in blog by user"""
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.blog}"
