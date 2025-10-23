# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Основные маршруты приложения
urlpatterns = [
    path("admin/", admin.site.urls),  # Административный интерфейс Django
    path("", include("map_app.urls")),  # Маршруты основного приложения карты
    path(
        "ckeditor5/", include("django_ckeditor_5.urls")
    ),  # Маршруты для загрузки файлов CKEditor
]

# В режиме разработки обслуживаем медиафайлы через Django
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
