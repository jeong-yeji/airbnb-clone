import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models as reservations_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates lireservations sts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reservations you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()+timedelta(days=random.randint(3, 25))
            },
        )
        seeder.execute()
        
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
