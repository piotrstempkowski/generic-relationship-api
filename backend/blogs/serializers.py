from django.contrib.auth.models import User
from rest_framework import serializers

from comments.serializers import CommentSerializer
# from likes.serializers import LikePublicSerializer
from .models import Blog

"""
I can't user LikePublicSerializer. I got circular import error:

  File "/code/accounts/urls.py", line 3, in <module>
    from .views import UserViewSet
  File "/code/accounts/views.py", line 5, in <module>
    from .serializers import UserSerializer
  File "/code/accounts/serializers.py", line 4, in <module>
    from blogs.serializers import BlogSerializer
  File "/code/blogs/serializers.py", line 5, in <module>
    from likes.serializers import LikePublicSerializer
  File "/code/likes/serializers.py", line 5, in <module>
    from blogs.serializers import BlogSerializer
ImportError: cannot import name 'BlogSerializer' from partially initialized module 'blogs.serializers' 
(most likely due to a circular import) (/code/blogs/serializers.py)
"""


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comments = CommentSerializer(many=True, read_only=True)
    # likes = LikePublicSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "author",
            "title",
            "content",
            "created_at",
            "comments",
            # "likes",
        ]
