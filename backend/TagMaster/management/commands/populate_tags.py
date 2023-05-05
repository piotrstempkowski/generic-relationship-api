from django.core.management import BaseCommand
from TagMaster.factories import TagItemFactory

class Command(BaseCommand):
    help = "populate database with tags"

    def handle(self, *args, **options):
        TagItemFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with tags."))