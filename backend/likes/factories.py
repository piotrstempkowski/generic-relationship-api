import factory
from django.contrib.contenttypes.fields import ContentType

from likes.models import Like


class LikeObjectFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory("accounts.factories.CustomUserFactory")
    object_id = factory.SelfAttribute('content_object.id')
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )


class LikedBlogFactory(LikeObjectFactory):
    content_object = factory.SubFactory("blogs.factories.BlogFactory")

    class Meta:
        model = Like


class LikedCommentFactory(LikeObjectFactory):
    content_object = factory.SubFactory("comments.factories.CommentFactory")

    class Meta:
        model = Like


class LikedReplyFactory(LikeObjectFactory):
    content_object = factory.SubFactory("replies.factories.ReplyFactory")

    class Meta:
        model = Like

# class LikeFactory(DjangoModelFactory):
#     class Meta:
#         model = Like
#
#     # author = factory.SubFactory(CustomUserFactory)
#     content_type = factory.Iterator(ContentType.objects.get_for_models(
#         Blog,
#         Comment,
#         Reply,
#     ).values())
#     object_id = factory.SelfAttribute('content_object.pk')
#     # content_object = factory.LazyAttribute(
#     #     lambda o: o.content_type.model_class().objects.get(pk=o.object_id)
#     # )
#
#
#     @factory.lazy_attribute
#     def author(self):
#         users = User.objects.all()
#         return random.choice(users)
#
#
#     @factory.lazy_attribute
#     def content_object(self):
#         model_class = self.content_type.model_class()
#         if model_class == Blog:
#             blogs = Blog.objects.all()
#             return random.choice(blogs)
#         elif model_class == Comment:
#             comments = Comment.objects.all()
#             return random.choice(comments)
#         elif model_class == Reply:
#             replies = Reply.objects.all()
#             return random.choice(replies)
#
#
#
# class ModelForTestsFactory(DjangoModelFactory):
#     class Meta:
#         model = Blog
#
#     author = factory.SubFactory("accounts.factories.CustomUserFactory")
#     title = factory.Sequence(lambda  n: f"Blog Title {n}")
#     content = factory.fuzzy.FuzzyText(length=30, chars=string.ascii_letters, prefix='')
#     created_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.UTC))
#     comments = factory.SubFactory("comments.factories.CommentFactory")
#     likes = factory.SubFactory("likes.factories.LikeFactory")
