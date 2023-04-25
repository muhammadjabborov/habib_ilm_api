from datetime import datetime

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse

from apps.shared.models import BaseModel
from apps.user.models import CourseComplain, CourseCategory, Teacher, Course, Student, CourseNew, Customer
from apps.user.resources import CustomerResource


@admin.register(CourseComplain)
class CourseComplainModelAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'description')
    fields = ('first_name', 'phone_number', 'description')
    ordering = ('id',)
    search_fields = ('first_name', 'phone_number', 'description')


@admin.register(CourseCategory)
class CourseCategoryModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'photo')
    fields = ('name', 'photo')
    exclude = ('slug',)
    search_fields = ('name', '')


@admin.register(Teacher)
class TeacherModelAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'direction')
    fields = ('full_name', 'direction', 'image', 'rating', 'description', 'url_video')
    ordering = ('id',)
    search_fields = ('full_name', 'description')


@admin.register(Course)
class CourseModelAdmin(ModelAdmin):
    list_display = ('title', 'duration', 'rating')
    fields = ('full_name', 'image', 'title', 'duration', 'rating', 'description', 'category')
    search_fields = ('title', 'description')


@admin.register(Student)
class StudentModelAdmin(ModelAdmin):
    list_display = ('full_name', 'teacher', 'course')
    search_fields = ('full_name',)


@admin.register(CourseNew)
class CourseNew(ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


def export_selected_purchased_courses(modeladmin, request, queryset):
    resource = CustomerResource()
    dataset = resource.export(queryset)
    response = HttpResponse(dataset.xlsx,
                            content_type='application/ms-excel')
    timestamp = datetime.now().strftime('%Y-%m-%d')
    response['Content-Disposition'] = f'attachment; filename="customers{timestamp}.xlsx"'
    return response


export_selected_purchased_courses.short_description = 'Export Customer to Excel'


@admin.register(Customer)
class CustomerModelAdmin(ModelAdmin):
    actions = (export_selected_purchased_courses,)
    list_display = ('first_name', 'phone_number')
    list_filter = ('status',)
    search_fields = ('first_name', 'phone_number')
