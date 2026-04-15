from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/courses/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', home_redirect),

    # كل شيء داخل app courses
    path('', include('courses.urls')),
]
