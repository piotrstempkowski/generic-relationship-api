from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
