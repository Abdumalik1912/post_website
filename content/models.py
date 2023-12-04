from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Images(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    image = models.ImageField(default="defaultimage.jpg")

    def __str__(self):
        return str(self.image)[:-4]
