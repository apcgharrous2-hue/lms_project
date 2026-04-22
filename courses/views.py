from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Course, Enrollment


# =========================
# CERTIFICATE (النسخة الصحيحة)
# =========================
@login_required
def certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return HttpResponse(
        f"Certificate: You completed {course.title}"
    )


# =========================
# LOGIN
# =========================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/courses/')

        return render(request, 'accounts/login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'accounts/login.html')


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('/login/')


# =========================
# COURSES LIST
# =========================
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses
    })


# =========================
# COURSE DETAIL
# =========================
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    # جلب الدروس (بدون شرط is_enrolled مؤقتاً)
    lessons = course.lessons.all().order_by('order')

    # حساب نسبة التقدم
    progress = 0

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_enrolled': is_enrolled,
        'lessons': lessons,
        'progress': progress,
    })
# =========================
# ENROLL
# =========================
# =========================
# ENROLL
# =========================
# =========================
# ENROLL
# =========================
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    # طريقة مباشرة بدون اسم المسار
    return redirect(f'/courses/{course_id}/')


# =========================
# UNENROLL
# =========================
@login_required
def unenroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.filter(
        student=request.user,
        course=course
    ).delete()

    # طريقة مباشرة بدون اسم المسار
    return redirect(f'/courses/{course_id}/')
# =========================
# MY COURSES
# =========================
@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, 'courses/my_courses.html', {
        'enrollments': enrollments
    })


# =========================
# MARK LESSON DONE
# =========================
@login_required
def mark_lesson_done(request, lesson_id):
    return redirect('/courses/')


# =========================
# EXAM
# =========================
@login_required
def course_exam(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(request, 'courses/exam.html', {
        'course': course
    })
