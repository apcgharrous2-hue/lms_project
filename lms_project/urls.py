from django.contrib import admin
from django.urls import path, include
from courses.views import my_courses  # ✅ استيراد الدالة

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('my-courses/', my_courses, name='my_courses'),  # ✅ أضف هذا
    path('', include('accounts.urls')),
]