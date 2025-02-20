from django.db import models

from core.constant import BlogStatusConst, CategoryConst


class Blog(models.Model):
    """ This model is used for the blog information"""
    title = models.CharField(max_length=64, null=True, blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    category =  models.CharField(max_length=10, choices=CategoryConst.choices(), null=True, blank=True)
    tags = models.ManyToManyField("Tag", null=True, blank=True)
    status = models.CharField(max_length=10, choices=BlogStatusConst.choices(), default="draft")

    def __str__(self):
        return self.title


class Tag(models.Model):
    """This model is used  for the tag"""
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
