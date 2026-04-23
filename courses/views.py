@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    # ✅ الدروس تظهر فقط إذا كان مسجلاً
    lessons = Lesson.objects.filter(course=course) if is_enrolled else []

    # حساب نسبة التقدم
    progress = 0
    if is_enrolled and lessons.exists():
        try:
            from .models import LessonProgress
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