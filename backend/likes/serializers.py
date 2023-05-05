from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.models import Blog
from blogs.serializers import BlogSerializer
from comments.models import Comment
from comments.serializers import CommentSerializer
from replies.models import Reply
from replies.serialiazers import ReplySerializer
from .models import Like


class LikeObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the 'liked object' generic relationship.
    """

    def to_representation(self, value):
        """
        Serialized liked object to simple textual representation.
        """
        if isinstance(value, Blog):
            # return f"Blog: {value}"
            serializer = BlogSerializer(value)
        elif isinstance(value, Comment):
            # return f"Comment: {value}"
            serializer = CommentSerializer(value)
        elif isinstance(value, Reply):
            # return f"Reply: {value}"
            serializer = ReplySerializer(value)
        else:
            raise Exception('Unexpected type of liked object.')

        return serializer.data


class LikeSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    # content_object = serializers.SerializerMethodField()
    content_object = LikeObjectRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Like
        fields = [
            "id",
            "author",
            "content_type",
            "object_id",
            "content_object",
            "created_at"
        ]

    def get_content_type(self, obj):
        return str(obj.content_type)

    # def get_content_object(self, obj):
    #     return str(obj.content_object)


class LikePublicSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    content_type = serializers.SerializerMethodField(read_only=True)
    content_object = LikeObjectRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = [
            "id",
            "author"
            "content_type",
            "object_id",
            "content_object",
            "created_at"
        ]

    def get_content_type(self, obj):
        return str(obj.content_type)
