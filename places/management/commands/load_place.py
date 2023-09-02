import json

import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = '''Add place from json
    json format:
    {
        "title": "",
        "imgs": ["url",],
        "description_short": "max length 350 ",
        "description_long": "HTMLField",
        "coordinates": 
            {
                "lng": "float",
                "lat": "float",
            },
    }
    '''

    def handle(self, *args, **options):
        if options['u']:
            response = requests.get(options['path'])
            place = response.json()
        else:
            with open(options['path'], 'r', encoding='UTF-8') as file:
                place = json.load(file)
        defaults = {
                'lat': place['coordinates']['lat'],
                'lng': place['coordinates']['lng'],
                'description_short': place['description_short'],
                'description_long': place['description_long'],
        }
        place_obj, created = Place.objects.update_or_create(title=place['title'], defaults=defaults)
        for img in place['imgs']:
            response = requests.get(img)
            response.raise_for_status()
            img = response.content
            img = ContentFile(img)
            place_image = place_obj.images.create()
            place_image.image.save(f'{place_obj.id}{place_image.id}.png', img)

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            help='path to json file'
        )
        parser.add_argument(
            '-u',
            '-url',
            action='store_true',
            help='For url path'
        )