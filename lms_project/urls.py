from django.core.management import call_command
from django.http import HttpResponse

def run_migrate(request):
    call_command('migrate', interactive=False)
    return HttpResponse("✅ Migrations done!")

urlpatterns = [
    path('run-migrate/', run_migrate),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('accounts.urls')),
]