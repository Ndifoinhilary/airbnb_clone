from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):
    help = 'This command create many facilities.'

    def handle(self, *args, **options):
        facilities = [
            'Private entrance',
            'Paid parking on premises',
            'Paid parking off premises',
            'Parking',
            'Elevator',
            'Gym'
        ]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Facilities were created successfully"))