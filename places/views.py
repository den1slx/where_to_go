from django.shortcuts import render

from places.models import Place, PlaceImage

# Create your views here.


def index(request):
    data = {
        'places': get_geo_places(),
    }
    return render(request, 'index.html', context=data)


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
                # 'detailsUrl': './static/places/moscow_legends.json',
                'detailsUrl': {
                    'title': place.title,
                    'imgs': get_images(place),
                    'description_short': place.description_short,
                    'description_long': place.description_long,
                },
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