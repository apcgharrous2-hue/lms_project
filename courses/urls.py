from django.urls import path
from .views import *
from django.http import HttpResponse

@login_required
def generate_certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return HttpResponse(
        f"Certificate: You completed {course.title}"
    )

urlpatterns = [
    path('courses/', course_list, name='courses'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),

    path('enroll/<int:course_id>/', enroll_course, name='enroll'),
    path('unenroll/<int:course_id>/', unenroll_course, name='unenroll'),

    path('lesson/done/<int:lesson_id>/', mark_lesson_done, name='mark_done'),

    path('my-courses/', my_courses, name='my_courses'),
     # ⭐ هذا مهم
    path('exam/<int:course_id>/', course_exam, name='exam'),
    path('certificate/<int:course_id>/', generate_certificate, name='certificate'),
    
]
