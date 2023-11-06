from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random  # Add this import
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models
from reservations import models as reservation_models

class Command(BaseCommand):
    help = 'This Love Django | creating a list of reservations'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', type=int, default=1, help='Creating a reservation of rooms'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        all_users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(reservation_models.Reservation, number, {
            'check_in': lambda x: timezone.now().date(),
            'check_out': lambda x: timezone.now().date() + timedelta(days=random.randint(3, 25)), 
            'guest': lambda x: random.choice(all_users),
            'room': lambda x: random.choice(rooms)
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(
            f"{number} reservations were created successfully"))
