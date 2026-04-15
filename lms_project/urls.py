from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/courses/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', home_redirect),

    # تطبيق courses
    path('', include('courses.urls')),
]
path('login/', login_view, name='login'),
path('logout/', logout_view, name='logout'),
