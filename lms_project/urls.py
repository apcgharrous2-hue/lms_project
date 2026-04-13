from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # لوحة الإدارة
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية → تحويل إلى الكورسات
    path('', lambda request: redirect('courses')),

    # روابط تطبيق courses
    path('', include('courses.urls')),
]