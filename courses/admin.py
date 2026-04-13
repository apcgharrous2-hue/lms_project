from django.contrib import admin
from .models import Course, Enrollment, Lesson
from .models import Question, Choice

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Choice)