from django.core.management import BaseCommand
from TagMaster.factories import BookmarkFactory

class Command(BaseCommand):
    help = "Populate database with bookmarks."

    def handle(self, *args, **options):
        BookmarkFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with bookmarks."))
