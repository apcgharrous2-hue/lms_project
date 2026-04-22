from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def run_migrate(request):
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms_project.settings')
    django.setup()
    
    from django.core.management import call_command
    call_command('migrate', interactive=False)
    
    return HttpResponse("✅ Migrations completed!")

urlpatterns = [
    path('run-migrate/', run_migrate),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('accounts.urls')),
]