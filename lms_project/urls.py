from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# مؤقت - احذفه بعد الاستخدام
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin123456')
        return HttpResponse("✅ Admin created! Username: admin, Password: Admin123456")
    else:
        User.objects.filter(username='admin').update(password=make_password('Admin123456'))
        return HttpResponse("✅ Admin password reset to: Admin123456")

def home_redirect(request):
    return redirect('/courses/')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_redirect),

    path('', include('courses.urls')),
    path('create-admin/', create_admin, name='create_admin'),
    path('', include('accounts.urls')),  # 👈 مهم جدًا
]
