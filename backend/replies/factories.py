import datetime
import string

import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Reply


class ReplyFactory(DjangoModelFactory):
    class Meta:
        model = Reply

    author = factory.SubFactory("accounts.factories.CustomUserFactory")
    comment = factory.SubFactory("comments.factories.CommentFactory")
    text = factory.fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    created_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.UTC))

    # @factory.lazy_attribute
    # def author(self):
    #     users = User.objects.all()
    #     return random.choice(users)
    #
    # @factory.lazy_attribute
    # def comment(self):
    #     comments = Comment.objects.all()
    #     return random.choice(comments)
