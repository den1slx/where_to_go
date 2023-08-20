from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import json
import requests
from PIL import Image
from io import BytesIO

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
        filtered_place = Place.objects.filter(
            lat=place['coordinates']['lat'],
            lng=place['coordinates']['lng'],
            title=place['title'],
        )
        if len(filtered_place) > 1:
            pass
        elif not filtered_place:
            Place.objects.create(
                lat=place['coordinates']['lat'],
                lng=place['coordinates']['lng'],
                title=place['title'],
                description_short=place['description_short'],
                description_long=place['description_long'],
            )
            created_place = Place.objects.filter(
                lat=place['coordinates']['lat'],
                lng=place['coordinates']['lng'],
                title=place['title'],
                description_short=place['description_short'],
                description_long=place['description_long'],
            ).first()
            for img in place['imgs']:
                response = requests.get(img)
                response.raise_for_status()
                img = response.content
                img = ContentFile(img)
                place_image = PlaceImage.objects.create(place=created_place)
                place_image.image.save(f'{created_place.id}{place_image.id}.png', img)
        else:
            place_obj = filtered_place.first()
            place_obj.lat = place['coordinates']['lat'],
            place_obj.lng = place['coordinates']['lng'],
            place_obj.title = place['title'],
            place_obj.description_short = place['description_short'],
            place_obj.description_long = place['description_long']
            # TODO avoid doubling images
            for img in place['imgs']:
                response = requests.get(img)
                response.raise_for_status()
                img = response.content
                img = ContentFile(img)
                place_image = PlaceImage.objects.create(place=place_obj)
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