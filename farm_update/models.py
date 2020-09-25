from django.db import models
from django.contrib.auth.models import User


class FarmUpdate(models.Model):
    post_title = models.CharField(max_length=255)
    post_body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_image = models.ImageField(null=True, blank=True)


    def __str__(self ):
        return self.post_title + '|' + self.author
