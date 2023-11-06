from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms.models import HouseRule


class Command(BaseCommand):
    help = 'This command create many house rule.'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int,
                            help='creating house rules')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(HouseRule, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            "house rules were created successfully"))
