from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Question, Lesson, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'created_at', 'students_count', 'status_badge']
    list_filter = ['created_at', 'instructor']
    search_fields = ['name', 'description', 'instructor__username']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('معلومات أساسية', {
            'fields': ('name', 'slug', 'description', 'instructor')
        }),
        ('الصور والوسائط', {
            'fields': ('image', 'thumbnail'),
            'classes': ('collapse',)
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def students_count(self, obj):
        return obj.enrollment_set.count()
    students_count.short_description = 'عدد الطلاب'
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: white; background: #10b981; padding: 5px 10px; border-radius: 5px;">✅ نشط</span>')
        return format_html('<span style="color: white; background: #ef4444; padding: 5px 10px; border-radius: 5px;">❌ غير نشط</span>')
    status_badge.short_description = 'الحالة'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_preview', 'course', 'question_type', 'difficulty_badge']
    list_filter = ['course', 'question_type', 'difficulty']
    search_fields = ['text', 'course__name']
    list_per_page = 20
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'السؤال'
    
    def difficulty_badge(self, obj):
        colors = {
            'easy': '#10b981',
            'medium': '#f59e0b',
            'hard': '#ef4444'
        }
        labels = {
            'easy': 'سهل',
            'medium': 'متوسط',
            'hard': 'صعب'
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.difficulty, '#6b7280'),
            labels.get(obj.difficulty, obj.difficulty)
        )
    difficulty_badge.short_description = 'الصعوبة'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content', 'course__name']
    ordering = ['course', 'order']
