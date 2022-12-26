import csv

from django.core.management.base import BaseCommand

from ads.models import Ad, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('category.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for d in data:
                category = Category(
                    name=d['name']
                )
                category.save()

        with open('ad.csv', encoding='utf-8') as file:
            data = csv.DictReader(file)

            for d in data:
                ad = Ad(
                    name=d['name'],
                    price=d['price'],
                    description=d['description'],
                    is_published=True if d['is_published'] == 'TRUE' else False,
                    image=d['image'],
                    author_id=d['author_id'],
                    category_id=d['category_id']
                )
                ad.save()


