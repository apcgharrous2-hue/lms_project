from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    # حذف المستخدم القديم إذا كان موجوداً
    User.objects.filter(username='admin').delete()
    
    # إنشاء مستخدم جديد
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin123456')
    
    return HttpResponse("✅ Admin created! Username: admin, Password: Admin123456")

urlpatterns = [
    path('create-admin/', create_admin),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('accounts.urls')),
]