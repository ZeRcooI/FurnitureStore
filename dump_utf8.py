import os
import django
from django.core.management import call_command
import io

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

# Убедимся, что папка существует
os.makedirs('fixtures/goods', exist_ok=True)

# Сохраняем дамп в UTF-8
with io.open('fixtures/goods/cats.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'goods.Categories', stdout=f)
