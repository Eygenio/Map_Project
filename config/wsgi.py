# config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Настройка переменной окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание WSGI приложения для развертывания на сервере
application = get_wsgi_application()