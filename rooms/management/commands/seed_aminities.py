from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = 'This is pure Django love.'

    def handle(self, *args, **options):
        amenities = [
            'Lock on bedroom door',
            'City skyline view',
            'Wifi',
            'Dedicated workspace',
            'TV',
            'Elevator',
            'Bathtub',
            'Hair dryer',
            'Refrigerator',
            'Microwave',
            'Dishes and silverware',
            'Bowls, chopsticks, plates',
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities were created successfully"))