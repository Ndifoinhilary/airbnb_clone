from django.core.management.base import BaseCommand
from django_seed import Seed
import  random
from users import models as user_models
from rooms import  models as room_models
from reviews import models as review_models
class Command(BaseCommand):
    help = 'This for the review model.'
    def add_arguments(self, parser) :
        parser.add_argument(
            '--number', type = int , default=1, help='creating reviews'
        )
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        all_rooms = room_models.Room.objects.all()
        all_users = user_models.User.objects.all()
        seeder.add_entity(review_models.Review, number,{
            'accuracy':lambda x : random.randint(1,5),
            'communication':lambda x : random.randint(1,5),
            'cleanliness':lambda x : random.randint(1,5),
            'location':lambda x : random.randint(1,5),
            'check_in':lambda x : random.randint(1,5),
            'value':lambda x : random.randint(1,5),
            'user':lambda x : random.choice(all_users),
            'room':lambda x : random.choice(all_rooms)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} were created successfully"))