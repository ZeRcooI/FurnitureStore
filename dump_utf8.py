import os
import django
from django.core.management import call_command
import io

# для запуска надо написать - python dump_utf8.py
# для заливки из json в бд, надо написать - python manage.py loaddata fixtures/goods/cats.json


# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

# Убедимся, что папка существует
os.makedirs('fixtures/goods', exist_ok=True)

# Сохраняем Categories в cats.json
with io.open('fixtures/goods/cats.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'goods.Categories', stdout=f)

# Сохраняем Products в prod.json
with io.open('fixtures/goods/prod.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'goods.Products', stdout=f)
