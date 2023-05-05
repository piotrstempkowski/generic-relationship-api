import datetime
import random
import string

import factory
from factory import fuzzy

# from comments.factories import CommentFactory
from .models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    author = factory.SubFactory("accounts.factories.CustomUserFactory")
    title = factory.Sequence(lambda n: f"Blog Title {n}")
    content = factory.fuzzy.FuzzyText(length=30, chars=string.ascii_letters, prefix='')
    created_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.UTC))

    class Params:
        no_comments = factory.Trait(
            comments=False,
        )
        no_likes = factory.Trait(
            likes=False
        )

    @factory.post_generation
    def comments(self, create, extracted, **kwargs):
        create_comments = getattr(self, "comments", True)
        if not create or not create_comments:
            return
        from comments.factories import CommentFactory
        comments = CommentFactory.create_batch(random.randint(5, 10), author=self.author, blog=self)
        return comments

    # @factory.post_generation
    # def likes(self, create, extractd, **kwargs):
    #     create_likes = getattr(self, "likes", True)
    #     if not create or not create_likes:
    #         return
    #     likes = LikeFactory.create_batch(10, author=self.author)
    #     return likes
