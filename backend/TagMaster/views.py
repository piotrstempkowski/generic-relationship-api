from rest_framework import viewsets

from .models import TaggedItem, Bookmark, Note
from .serializers import TaggedObjectedRelateFieldNestedSerializers, BookmarkSerializer, NoteSerializer


class TaggedItemViewSet(viewsets.ModelViewSet):
    queryset = TaggedItem.objects.all()
    serializer_class = TaggedObjectedRelateFieldNestedSerializers


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
