import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            name = phone['name']
            price = int(phone['price'])
            image = phone['image']
            release_date = phone['release_date']
            slug = slugify(phone["name"])
            if phone['lte_exists'] == "False":
                lte_exists = False
            else:
                lte_exists = True
            ph = Phone(name=name, price=price, image=image, release_date=release_date, lte_exists=lte_exists, slug=slug)
            ph.save()

