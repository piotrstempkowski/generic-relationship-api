from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
