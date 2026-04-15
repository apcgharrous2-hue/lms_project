from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='courses'),
    path('course/<int:course_id>/', views.course_detail),

    path('enroll/<int:course_id>/', views.enroll_course),
    path('unenroll/<int:course_id>/', views.unenroll_course),

    path('lesson/done/<int:lesson_id>/', views.mark_lesson_done),

    path('my-courses/', views.my_courses),

    path('exam/<int:course_id>/', views.course_exam),

    path('certificate/<int:course_id>/', views.certificate),
]
