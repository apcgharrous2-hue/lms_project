from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import Course, Lesson, Enrollment, Progress
from .models import Question, Choice


# 📚 جميع الكورسات
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# 📖 تفاصيل الكورس + الدروس + التقدم
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)

    # هل الطالب مسجل؟
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    # حساب التقدم
    total_lessons = lessons.count()

    done_lessons = Progress.objects.filter(
        student=request.user,
        course=course
    ).count()

    progress = 0
    if total_lessons > 0:
        progress = int((done_lessons / total_lessons) * 100)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled,
        'progress': progress
    })


# ✅ تسجيل في الكورس
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect('course_detail', course_id=course.id)


# ❌ إلغاء التسجيل
@login_required
def unenroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.filter(
        student=request.user,
        course=course
    ).delete()

    return redirect('course_detail', course_id=course.id)


# ✔ تسجيل مشاهدة الدرس
@login_required
def mark_lesson_done(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    Progress.objects.get_or_create(
        student=request.user,
        course=lesson.course,
        lesson=lesson
    )

    return redirect('course_detail', course_id=lesson.course.id)


# 🎓 كورساتي
@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {
        'enrollments': enrollments
    })


# 🎓 إنشاء شهادة PDF
@login_required
def generate_certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)

    total = lessons.count()

    done = Progress.objects.filter(
        student=request.user,
        course=course
    ).count()

    # ❌ لم يكمل
    if total == 0 or done < total:
        return HttpResponse("❌ لم تكمل الدورة بعد")

    # ✅ إنشاء PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("🎓 Certificate of Completion", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Student: {request.user}", styles['Normal']))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Course: {course.title}", styles['Normal']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Congratulations for completing the course!", styles['Normal']))

    doc.build(content)

    return response
@login_required
def course_exam(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = Question.objects.filter(course=course)

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=selected)
                if choice.is_correct:
                    score += 1

        return render(request, 'courses/exam_result.html', {
            'score': score,
            'total': total
        })

    return render(request, 'courses/exam.html', {
        'course': course,
        'questions': questions
    })