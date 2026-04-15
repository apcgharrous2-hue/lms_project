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
path('login/', login_view, name='login'),
path('logout/', logout_view, name='logout'),
path('login/', login_view),
path('logout/', logout_view),

path('courses/', course_list, name='courses'),
path('course/<int:course_id>/', course_detail),
path('enroll/<int:course_id>/', enroll_course),
path('unenroll/<int:course_id>/', unenroll_course),
path('my-courses/', my_courses),
path('exam/<int:course_id>/', course_exam),
path('certificate/<int:course_id>/', certificate),
]
