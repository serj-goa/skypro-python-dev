import csv
from django.core.management.base import BaseCommand
from user.models import Location, User

class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('location.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for d in data:
                location = Location(
                    name=d['name'],
                    lat=d['lat'],
                    lng=d['lng']
                )
                location.save()

        with open('user.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for d in data:
                user = User(
                    first_name=d['first_name'],
                    last_name=d['last_name'],
                    username=d['username'],
                    role=d['role'],
                    age=d['age']
                )
                user.set_password(d['password'])
                user.save()
                user.location.add(Location.objects.get(pk=d['location_id']))
                user.save()
