from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('courses/')  # أو dashboard حسب مشروعك

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_redirect),

    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
]
