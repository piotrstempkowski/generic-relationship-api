from django.core.management import BaseCommand
from comments.factories import CommentFactory

class Command(BaseCommand):
    help = "Populate database with comments"

    def handle(self, *args, **options):
        CommentFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Successfully populated comments."))