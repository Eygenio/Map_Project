# map_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('places/', views.places_geojson, name='places_geojson'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
