# config/settings.py
import os
from pathlib import Path

# Базовый путь проекта - корневая директория Django проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для криптографических операций Django
# В продакшене должен быть скрыт в переменных окружения
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key-for-dev")
DEBUG = os.getenv("DEBUG", "True") == "True"

# SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
# DEBUG = False

# Список разрешенных доменов для работы приложения
# Защищает от атак подмены хоста
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ALLOWED_HOSTS = [
#     "www.Eygenio.pythonanywhere.com",
#     "Eygenio.pythonanywhere.com",
# ]

# Зарегистрированные приложения Django
INSTALLED_APPS = [
    "django.contrib.admin",  # Административный интерфейс
    "django.contrib.auth",  # Система аутентификации и авторизации
    "django.contrib.contenttypes",  # Система типов контента для общих отношений
    "django.contrib.sessions",  # Механизм сессий для хранения состояния
    "django.contrib.messages",  # Фреймворк системных сообщений
    "django.contrib.staticfiles",  # Обработчик статических файлов (CSS, JS, изображения)
    "map_app",  # Основное приложение карты с моделями мест
    "django_ckeditor_5",  # WYSIWYG редактор для форматирования текстов
]

# Промежуточное ПО - обработчики запросов/ответов
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Безопасность: HTTPS, HSTS и др.
    "django.contrib.sessions.middleware.SessionMiddleware",  # Управление сессиями пользователей
    "django.middleware.common.CommonMiddleware",  # Стандартные операции с URL
    "django.middleware.csrf.CsrfViewMiddleware",  # Защита от CSRF атак
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Аутентификация пользователей
    "django.contrib.messages.middleware.MessageMiddleware",  # Обработка системных сообщений
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от clickjacking через iframe
]

# Корневой модуль маршрутизации URL
ROOT_URLCONF = "config.urls"

# Конфигурация системы шаблонов
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Движок шаблонов Django
        "DIRS": [BASE_DIR / "templates"],  # Дополнительные директории с шаблонами
        "APP_DIRS": True,  # Автопоиск шаблонов в папках templates приложений
        "OPTIONS": {
            "context_processors": [  # Процессоры контекста для глобальных переменных в шаблон
                "django.template.context_processors.debug",  # Переменная debug
                "django.template.context_processors.request",  # Объект запроса
                "django.contrib.auth.context_processors.auth",  # Информация о пользователе
                "django.contrib.messages.context_processors.messages",  # Системные сообщения
            ],
        },
    },
]

# Настройки базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Движок SQLite для разработки
        "NAME": BASE_DIR / "db.sqlite3",  # Путь к файлу базы данных
    }
}

# Настройки статических файлов (CSS, JavaScript, изображения)
STATIC_URL = "/static/"  # Базовый URL для статических файлов
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Дополнительные директории со статическими файлами
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Директория для сбора статики в продакшене

# Настройки медиафайлов (загружаемые пользователями изображения)
MEDIA_URL = "/media/"  # Базовый URL для медиафайлов
MEDIA_ROOT = BASE_DIR / "media"  # Директория для хранения загруженных файлов

# Палитра пользовательских цветов для CKEditor 5
customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
]

# Конфигурация CKEditor 5 - WYSIWYG редактора
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
        ],
        "height": 300,
    },
}
