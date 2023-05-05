from django.contrib.auth.models import User
from django.db import models

from blogs.models import Blog


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} commend: {self.text}"
