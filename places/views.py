from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from places.models import Place, PlaceImage

import json

# Create your views here.


def index(request):
    data = {
        'places': get_geo_places(),
    }
    return render(request, 'index.html', context=data)


def place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except ObjectDoesNotExist:
        raise Http404

    return HttpResponse(get_place_info(place), content_type="application/json")


def get_geo_places():
    places = Place.objects.all()
    features = []
    for place in places:
        place = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': f'{place.id}',
                'detailsUrl': f'./place/{place.id}',
                # 'detailsUrl': {
                #     'title': place.title,
                #     'imgs': get_images(place),
                #     'description_short': place.description_short,
                #     'description_long': place.description_long,
                # },
            }
        }

        features.append(place)

    geo_json = {
        'type': 'FeatureCollection',
        'features': features
    }
    return geo_json


def get_images(place):
    place_images = PlaceImage.objects.filter(place=place)
    imgs = [f'media/{place.image}' for place in place_images]
    return imgs


def get_place_info(place):

    place_info = {
        "title": place.title,
        'imgs': get_images(place),
        "description_short": place.description_short,
        "description_long": place.tmc,
        # "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        }
    }
    place_info = json.dumps(place_info, ensure_ascii=False, indent=4)
    return place_info



