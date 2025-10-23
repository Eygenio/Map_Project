# map_app/management/commands/load_place.py
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from map_app.models import Place, Image
import json


class Command(BaseCommand):
    """Кастомная команда Django для загрузки данных мест из JSON URL"""

    help = "Load place data from JSON URL"

    def add_arguments(self, parser):
        """Добавление аргументов командной строки"""

        parser.add_argument("url", type=str, help="URL to JSON file")

    def handle(self, *args, **options):
        """Основной обработчик команды"""

        url = options["url"]

        try:
            response = requests.get(url)
            response.raise_for_status()
            place_data = response.json()

            # Создаем или обновляем место
            place, created = Place.objects.get_or_create(
                title=place_data["title"],
                defaults={
                    "description_short": place_data.get("description_short", ""),
                    "description_long": place_data.get("description_long", ""),
                    "lng": place_data["coordinates"]["lng"],
                    "lat": place_data["coordinates"]["lat"],
                },
            )

            # Загружаем изображения
            for img_url in place_data["imgs"]:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_name = img_url.split("/")[-1]
                image = Image(place=place)
                image.image.save(img_name, ContentFile(img_response.content), save=True)

            action = "создано" if created else "обновлено"
            self.stdout.write(
                self.style.SUCCESS(f'Место "{place.title}" успешно {action}')
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке данных: {str(e)}"))
