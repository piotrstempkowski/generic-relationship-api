import factory
from django.contrib.contenttypes.models import ContentType
from factory import fuzzy

from .models import TaggedItem, Bookmark, Note


class BookmarkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bookmark

    url = factory.Faker("url")


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    text = factory.fuzzy.FuzzyText(length=12)


class TaggedItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaggedItem
        # exclude = ["content_object"]
        # abstract = True

    tag = factory.Faker("slug")
    object_id = factory.SelfAttribute('content_object.id')
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )


class TaggedBookmarkFactory(TaggedItemFactory):
    content_object = factory.SubFactory(BookmarkFactory)

    class Meta:
        model = TaggedItem


class TaggedNoteFactory(TaggedItemFactory):
    content_object = factory.SubFactory(NoteFactory)

    class Meta:
        model = TaggedItem

# class TagItemFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = TaggedItem
#
#     tag = factory.Faker("slug")
#     object_id = factory.SelfAttribute('content_object.id')
#     content_type = factory.Iterator(ContentType.objects.get_for_models(
#         Bookmark,
#         Note,
#     ).values())
#
#     @factory.lazy_attribute
#     def content_object(self):
#         model_class = self.content_type.model_class()
#         if model_class == Bookmark:
#             bookmarks = Bookmark.objects.all()
#             return random.choice(bookmarks)
#         elif model_class == Note:
#            notes = Note.objects.all()
#            return random.choice(notes)
