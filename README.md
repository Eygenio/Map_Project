# Map_Project - Карта интересных мест Москвы

🗺️ Интерактивная карта Москвы с точками активного отдыха от блогера Артёма.

## 🌐 Демо-версия

**Рабочий сайт:** [https://Eygenio.pythonanywhere.com/](https://Eygenio.pythonanywhere.com/)

**Тестовые данные:**
- Главная страница с картой: [https://Eygenio.pythonanywhere.com/](https://Eygenio.pythonanywhere.com/)
- Админка Django: [https://Eygenio.pythonanywhere.com/admin/](https://Eygenio.pythonanywhere.com/admin/)
- API всех мест: [https://Eygenio.pythonanywhere.com/places/](https://Eygenio.pythonanywhere.com/places/)
- API деталей места: [https://Eygenio.pythonanywhere.com/places/1/](https://Eygenio.pythonanywhere.com/places/8/)

## Особенности

- 🗺️ Интерактивная карта с метками интересных мест
- 📍 Боковая панель с детальной информацией о местах
- 🖼️ Drag & Drop сортировка изображений в админке
- 📱 Адаптивный дизайн для всех устройств
- 🔧 Удобная админка с WYSIWYG редактором
- 🗄️ REST API для интеграции с фронтендом

## Архитектура

- **Django 5.0**: Backend фреймворк с ORM
- **SQLite**: База данных для хранения мест и изображений
- **Leaflet.js**: Интерактивная карта с OpenStreetMap
- **Sortable.js**: Drag & Drop сортировка в админке
- **CKEditor 5**: WYSIWYG редактор для описаний
- **Pillow**: Обработка и хостинг изображений

## Функциональность

## Для пользователей
- Просмотр всех мест на интерактивной карте
- Детальная информация о каждом месте в боковой панели
- Просмотр фотографий и описаний
- Адаптивный интерфейс для мобильных устройств

## Для администраторов
- Удобное добавление и редактирование мест
- Drag & Drop сортировка изображений
- WYSIWYG редактор для HTML-описаний
- Превью изображений в админке
- Загрузка данных из JSON через команду

## Запуск проекта

1. Клонирование репозитория
```bash
git clone https://github.com/Eygenio/Map_Project
cd Map_Project
```
2. Создание виртуального окружения и установка зависимостей:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Настройка базы данных:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Создание суперпользователя:
```bash
python manage.py createsuperuser
```
5. Сбор статических файлов:
```bash
python manage.py collectstatic --noinput
```
6. Запуск сервера:
```bash
python manage.py runserver
```
## Доступ к сервисам
- **Главная страница:** http://127.0.0.1:8000/
- **Админка Django:** http://127.0.0.1:8000/admin/
- **API всех мест (GeoJSON):** http://127.0.0.1:8000/places/
- **API деталей места:** http://127.0.0.1:8000/places/1/
- 
## Использование
1. Войдите в админку Django
2. Перейдите в раздел "Места"
3. Нажмите "Добавить место"
4. Заполните информацию о месте:
   - Название
   - Короткое и полное описание (с WYSIWYG редактором)
   - Координаты (широта и долгота)
   - Загрузите изображения с возможностью перетаскивания для сортировки


## Загрузка данных из JSON
```bash
python manage.py load_place <URL_к_JSON_файлу>
```

## API Endpoints 
- `GET /places/` - возвращает все места в формате GeoJSON
- `GET /places/<id>/` - возвращает детальную информацию о месте

## Технические особенности
- Язык: Python 3.13
- Фреймворк: Django 5.0.1
- База данных: SQLite с миграциями
- Фронтенд: Leaflet.js для карт, чистый JavaScript
- Медиафайлы: Хостинг изображений через Django MEDIA
- Сортировка: Sortable.js для Drag & Drop в админке
- Редактор: CKEditor 5 для WYSIWYG редактирования
