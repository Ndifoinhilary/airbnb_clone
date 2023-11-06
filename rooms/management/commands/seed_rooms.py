from django.core.management.base import BaseCommand, CommandParser
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_model
from users import models as user_model
import random


class Command(BaseCommand):
    help = 'This command create many facilities.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', default=1,
                            type=int, help='creating rooms')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        all_users = user_model.User.objects.all()
        room_types = room_model.RoomType.objects.all()
        amenities = room_model.Amenity.objects.all()
        amenities_count = room_model.Amenity.objects.all().count()
        house_rules = room_model.HouseRule.objects.all()
        house_rules_count = room_model.HouseRule.objects.all().count()
        all_facilities = room_model.Facility.objects.all()
        all_facilities_count = room_model.Facility.objects.all().count()
        seeder.add_entity(room_model.Room, number, {
            'guests':lambda x : random.randint(1,5),
             'beds':lambda x : random.randint(1,5),
            'bedroom':lambda x : random.randint(1,5),
             'baths':lambda x : random.randint(1,5),
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'roomtype': lambda x: random.choice(room_types),
        })
        create_room = seeder.execute()
        clean_room = flatten(list(create_room.values()))
        for pk in clean_room:
            room = room_model.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f'photos/{random.randint(1,17)}.webp',
                    room=room
                )
            for a in amenities:
                magic_number = random.randint(0, amenities_count)
                if magic_number % 2 != 0:
                    room.amenities.add(a)
            for f in all_facilities:
                magic_number = random.randint(0, all_facilities_count)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for h in house_rules:
                magic_number = random.randint(0, house_rules_count)
                if magic_number % 2 == 0:
                    room.house_rule.add(h)
        self.stdout.write(self.style.SUCCESS(
            "rooms  were created successfully"))
