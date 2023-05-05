from django.core.management import BaseCommand
from replies.factories import ReplyFactory

class Command(BaseCommand):
    help = "Populate database with replies"

    def handle(self, *args, **options):
        ReplyFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with replies."))


