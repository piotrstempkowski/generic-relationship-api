import factory
import random
from factory.django import DjangoModelFactory

from blogs.factories import BlogFactory
from comments.factories import CommentFactory
from likes.factories import LikedBlogFactory, LikedCommentFactory, LikedReplyFactory
from replies.factories import ReplyFactory


class BaseFactory(DjangoModelFactory):
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
        blogs = BlogFactory.create_batch(random.randint(1, 3), author=self)
        for blog in blogs:
            CommentFactory.create_batch(random.randint(1, 2), author=self, blog=blog)
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
        liked_blog = LikedBlogFactory.create_batch(3, author=self)
        liked_comments = LikedCommentFactory.create_batch(3, author=self)
        liked_replies = LikedReplyFactory.create_batch(3, author=self)
        return liked_blog, liked_comments, liked_replies