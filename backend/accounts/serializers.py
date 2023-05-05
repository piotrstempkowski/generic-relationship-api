from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.serializers import BlogSerializer
from comments.serializers import CommentSerializer
from likes.serializers import LikeSerializer
from replies.serialiazers import ReplySerializer


class UserSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "last_login",
            "blogs",
            "comments",
            "replies",
            "likes",
        ]
