from django.db import models


class Comment(models.Model):
    """This is  the comment model that added in blog by user"""
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    text = models.TextField()

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.blog}"
