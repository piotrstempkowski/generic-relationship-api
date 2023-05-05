from django.core.management import BaseCommand
from likes.factories import LikeFactory

class Command(BaseCommand):
    help = "Populate database with likes"

    def handle(self, *args, **options):
        LikeFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Populate database with likes."))


