from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # الصفحة الرئيسية للدورات
    path('', views.course_list, name='course_list'),

    # تفاصيل الدورة
    path('<int:course_id>/', views.course_detail, name='course_detail'),

    # التسجيل في الدورة
    path('<int:course_id>/enroll/', views.enroll_course, name='enroll'),

    # إلغاء التسجيل
    path('<int:course_id>/unenroll/', views.unenroll_course, name='unenroll'),

    # تحديد الدرس كمكتمل
    path('lesson/<int:lesson_id>/done/', views.mark_lesson_done, name='mark_done'),

    # دوراتي
    path('my-courses/', views.my_courses, name='my_courses'),

    # الامتحان
    path('<int:course_id>/exam/', views.course_exam, name='exam'),

    # الشهادة
    path('<int:course_id>/certificate/', views.certificate, name='certificate'),
]