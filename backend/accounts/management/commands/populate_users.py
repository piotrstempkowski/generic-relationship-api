from django.core.management import BaseCommand
from blogs.factories import CustomUserFactory


class Command(BaseCommand):
    help = "Populate database with blogs."

    def handle(self, *args, **options):

        CustomUserFactory.create_batch(20)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with users."))