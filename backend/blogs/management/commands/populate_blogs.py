from django.core.management import BaseCommand
from django.contrib.auth.models import User
from blogs.factories import BlogFactory, CustomUserFactory


class Command(BaseCommand):
    help = "Populate database with blogs."

    def handle(self, *args, **options):

        BlogFactory.create_batch(20)

        self.stdout.write(self.style.SUCCESS("Successfully populated authors with blogs"))