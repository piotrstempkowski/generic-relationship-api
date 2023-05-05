from django.core.management import BaseCommand
from TagMaster.factories import TaggedBookmarkFactory, TaggedNoteFactory


class Command(BaseCommand):
    help = "Populated database with taggedItem"

    def handle(self, *args, **options):
        TaggedBookmarkFactory.create_batch(10)
        TaggedNoteFactory.create_batch(10)



        self.stdout.write(self.style.SUCCESS("Populate database with Tags, Bookmarks, Notes."))