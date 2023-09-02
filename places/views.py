import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, PlaceImage


def index(request):
    context = {
        'places': get_geo_places(),
    }
    return render(request, 'index.html', context=context)


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_images = place.images.all()
    imgs = [place.image.url for place in place_images]

    place_json = {
        "title": place.title,
        'imgs': imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        }
    }
    place_json = json.dumps(place_json, ensure_ascii=False, indent=4)

    return HttpResponse(place_json, content_type="application/json")


def get_geo_places():
    places = Place.objects.all()
    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': f'{place.id}',
                'detailsUrl': reverse('place', args=(place.id,))
            }
        } for place in places]

    geo_json = {
        'type': 'FeatureCollection',
        'features': features
    }
    return geo_json
