from django.urls import path
from . import views  # استيراد جميع الدوال من views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),           # الصفحة الرئيسية بعد تسجيل الدخول
    path('login/', views.login_view, name='login'),        # تسجيل الدخول
    path('logout/', views.logout_view, name='logout'),     # تسجيل الخروج
    path('register/', views.register_view, name='register'), # تسجيل حساب جديد
]