import datetime
import string

import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Comment


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory("accounts.factories.CustomUserFactory")
    text = factory.fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    blog = factory.SubFactory("blogs.factories.BlogFactory")
    created_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.UTC))

    class Params:
        no_blogs = factory.Trait(
            blogs=False,
        )

    # @factory.post_generation
    # def author(self, create, extracted, **kwargs):
    #     create_author = getattr(self, "author", True)
    #     if not create or not create_author:
    #         return
    #     self.author = accounts.factories.CustomUserFactory()  # Set the author attribute directly
    #     self.save()

    # @factory.post_generation
    # def blogs(self, create, extracted, **kwargs):
    #     create_blogs = getattr(self, "blogs", True)
    #     if not create or not create_blogs:
    #         return
    #     blogs = BlogFactory.create_batch(random.randint(1, 3), comments=self)
    #     return blogs
