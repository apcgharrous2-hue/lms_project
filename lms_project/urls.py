from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.models import User

# مؤقت - احذفه بعد الاستخدام
def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin123456')
        return HttpResponse("✅ Admin created! Username: admin, Password: Admin123456")
    else:
        # تحديث كلمة السر
        u = User.objects.get(username='admin')
        u.set_password('Admin123456')
        u.save()
        return HttpResponse("✅ Admin password reset to: Admin123456")

urlpatterns = [
    path('create-admin/', create_admin, name='create_admin'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('accounts.urls')),
]