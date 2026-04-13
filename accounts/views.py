from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from courses.models import Course, Enrollment


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'خطأ في البيانات'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_courses = Course.objects.count()
    total_students = Enrollment.objects.count()
    my_courses = Enrollment.objects.filter(student=request.user).count()

    context = {
        'total_courses': total_courses,
        'total_students': total_students,
        'my_courses': my_courses
    }

    if hasattr(request.user, 'is_teacher') and request.user.is_teacher:
        return render(request, 'accounts/dashboard_teacher.html', context)

    return render(request, 'accounts/dashboard_student.html', context)