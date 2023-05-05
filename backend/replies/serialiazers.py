from rest_framework import serializers

from .models import Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            "id",
            "author",
            "comment",
            "text",
            "created_at",
        ]
