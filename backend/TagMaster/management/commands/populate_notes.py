from django.core.management import BaseCommand
from TagMaster.factories import NoteFactory


class Command(BaseCommand):
    help = "Populate database with notes"

    def handle(self, *args, **options):
        NoteFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS("Successfully populated database with notes."))