# map_app/urls.py
from django.urls import path
from . import views

# Маршруты основного приложения карты
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # Главная страница с картой
    path(
        "places/", views.places_geojson, name="places_geojson"
    ),  # API всех мест (GeoJSON)
    path(
        "places/<int:place_id>/", views.place_detail, name="place_detail"
    ),  # API деталей места
]
