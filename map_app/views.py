# map_app/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Place, Image
import json


class IndexView(TemplateView):
    """Главная страница с картой - использует шаблонный класс Django"""

    template_name = 'index.html'


def places_geojson(request):
    """API endpoint для получения всех мест в формате GeoJSON"""

    places = Place.objects.prefetch_related('images').all()

    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/places/{place.id}/"
            }
        }
        features.append(feature)

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson_data, json_dumps_params={'ensure_ascii': False})


def place_detail(request, place_id):
    """API endpoint для получения детальной информации о конкретном месте"""

    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)

    place_data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(
        place_data,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
