from django.contrib import admin
from .models import Course, Question, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'instructor']
    search_fields = ['instructor__username']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'course']
    search_fields = ['text']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course']
    search_fields = ['title']