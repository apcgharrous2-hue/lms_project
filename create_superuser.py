import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms_project.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
email = 'admin@example.com'
password = 'Admin123456'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✅ Superuser "{username}" created successfully!')
else:
    print(f'⚠️ Superuser "{username}" already exists.')
