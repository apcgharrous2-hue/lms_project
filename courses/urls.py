from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='courses'),

    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    path('enroll/<int:course_id>/', views.enroll_course, name='enroll'),

    path('unenroll/<int:course_id>/', views.unenroll_course, name='unenroll'),

    path('lesson/done/<int:lesson_id>/', views.mark_lesson_done, name='mark_done'),

    path('my-courses/', views.my_courses, name='my_courses'),

    path('exam/<int:course_id>/', views.course_exam, name='exam'),

    path('certificate/<int:course_id>/', views.certificate, name='certificate'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
]
