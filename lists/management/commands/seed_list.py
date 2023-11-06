from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
import random
from users import models as user_models
from rooms import models as room_models
from lists import models as list_models


class Command(BaseCommand):
    help = 'This Love Django |  creating list of rooms'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', type=int, default=1, help='Creating a list of rooms'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        all_users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(list_models.List, number, {
            'user': lambda x: random.choice(all_users)
        })
        create_list = seeder.execute()
        all_list_pk = flatten(list(create_list.values()))
        for pk in all_list_pk:
            lists = list_models.List.objects.get(pk=pk)
            list_room = rooms[random.randint(0, 5): random.randint(5, 10)]
            lists.rooms.add(*list_room)
        self.stdout.write(self.style.SUCCESS(
            f"{number} were created successfully"))
