from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/courses/')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_redirect),

    path('', include('courses.urls')),
    path('', include('accounts.urls')),  # 👈 مهم جدًا
]
