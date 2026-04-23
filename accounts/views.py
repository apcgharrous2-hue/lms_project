from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from courses.models import Course, Enrollment


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/dashboard/')
            return redirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': 'خطأ في البيانات'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email', '')

        # ✅ التحقق من عدم وجود مستخدم بنفس الاسم
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': f'اسم المستخدم "{username}" موجود مسبقاً. اختر اسماً آخر.'
            })

        # إنشاء مستخدم جديد
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # تسجيل الدخول تلقائياً
        login(request, user)
        
        # العودة إلى لوحة التحكم
        return redirect('/dashboard/')
    
    return render(request, 'accounts/register.html')

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