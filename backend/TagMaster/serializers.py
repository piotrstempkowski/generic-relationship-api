from rest_framework import serializers

from .models import Bookmark, Note


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = [
            "id",
            "url",
            "tags",
        ]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            "id",
            "text",
            "tags",
        ]


class TaggedObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for tagged object generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged object to a simple textual representation.
        """
        if isinstance(value, Bookmark):
            return f"Bookmark: {value.url}"
        elif isinstance(value, Note):
            return f"Note: {value.text}"
        raise Exception("Unexpected type of tagged object")


class TaggedObjectedRelateFieldNestedSerializers(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, Bookmark):
            serializer = BookmarkSerializer(value)
        elif isinstance(value, Note):
            serializer = NoteSerializer(value)
        else:
            raise Exception("Unexpected type of tagged object")

        return serializer.data
