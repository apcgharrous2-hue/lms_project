from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Course, Enrollment, Lesson, Question, LessonProgress


# =========================
# CERTIFICATE
# =========================
@login_required
def certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return HttpResponse(f"Certificate: You completed {course.title}")


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
            
            # العودة إلى الصفحة المطلوبة أو الرئيسية
            next_url = request.GET.get('next', '/courses/')
            return redirect(next_url)

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
# REGISTER
# =========================
def register_view(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email', '')
        
        # إنشاء مستخدم جديد
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # تسجيل الدخول تلقائياً
        login(request, user)
        
        # العودة إلى الصفحة المطلوبة أو الرئيسية
        next_url = request.GET.get('next', '/courses/')
        return redirect(next_url)
    
    return render(request, 'accounts/register.html')


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

    # التحقق من التسجيل
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    # الدروس تظهر فقط إذا كان مسجلاً
    lessons = Lesson.objects.filter(course=course).order_by('id') if is_enrolled else []

    # حساب نسبة التقدم
    progress = 0
    if is_enrolled and lessons.exists():
        try:
            completed = LessonProgress.objects.filter(
                user=request.user,
                lesson__course=course,
                completed=True
            ).count()
            progress = int((completed / lessons.count()) * 100) if lessons.count() > 0 else 0
        except:
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
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect('courses:course_detail', course_id=course_id)


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

    return redirect('courses:course_detail', course_id=course_id)


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
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # التحقق من التسجيل في الدورة
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=lesson.course
    ).exists()

    if not is_enrolled:
        return redirect('courses:course_detail', course_id=lesson.course.id)

    # تسجيل التقدم
    progress, created = LessonProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )
    progress.completed = True
    progress.save()

    return redirect('courses:course_detail', course_id=lesson.course.id)


# =========================
# EXAM
# =========================
@login_required
def course_exam(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # التحقق من التسجيل
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    if not is_enrolled:
        return redirect('courses:course_detail', course_id=course_id)

    questions = Question.objects.filter(course=course)

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for q in questions:
            selected = request.POST.get(f'q_{q.id}')
            if selected == q.correct_option:
                score += 1
        
        percentage = int((score / total) * 100) if total > 0 else 0

        return render(request, 'courses/exam_result.html', {
            'course': course,
            'score': score,
            'total': total,
            'percentage': percentage
        })

    return render(request, 'courses/exam.html', {
        'course': course,
        'questions': questions
    })