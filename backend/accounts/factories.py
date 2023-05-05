import random

import factory
from django.contrib.auth.models import User

from blogs.factories import BlogFactory
from comments.factories import CommentFactory
from likes.factories import LikedBlogFactory, LikedCommentFactory, LikedReplyFactory
from replies.factories import ReplyFactory


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "password123")

    class Params:
        no_blogs = factory.Trait(
            blogs=False,
        )
        no_comments = factory.Trait(
            comments=False
        )
        no_replies = factory.Trait(
            replies=False
        )
        no_likes = factory.Trait(
            likes=False
        )

    @factory.post_generation
    def blogs(self, create, extracted, **kwargs):
        create_blogs = getattr(self, "blogs", True)
        if not create or not create_blogs:
            return

        blogs = BlogFactory.create_batch(random.randint(5, 10), author=self)
        for blog in blogs:
            CommentFactory.create_batch(random.randint(5, 10), author=self, blog=blog)
        return blogs

    @factory.post_generation
    def comments(self, create, extracted, **kwargs):
        create_comments = getattr(self, "comments", True)
        if not create or not create_comments:
            return
        comments = CommentFactory.create_batch(random.randint(5, 10), author=self, blog=random.choice(self.blogs.all()))
        return comments

    @factory.post_generation
    def replies(self, create, extracted, **kwargs):
        create_replies = getattr(self, "replies", True)
        if not create or not create_replies:
            return
        for comment in self.comments.all():
            replies = ReplyFactory.create_batch(random.randint(5, 10), author=self, comment=comment)
            return replies

    @factory.post_generation
    def likes(self, create, extracted, **kwargs):
        create_likes = getattr(self, "likes", True)
        if not create or not create_likes:
            return
        user_likes = []

        """
        Creates likes for your own user objects
        """

        for blog in self.blogs.all():
            user_likes.append(LikedBlogFactory(author=self, content_object=blog))

        for comment in self.comments.all():
            user_likes.append(LikedCommentFactory(author=self, content_object=comment))

        for reply in self.replies.all():
            user_likes.append(LikedReplyFactory(author=self, content_object=reply))

        return user_likes
