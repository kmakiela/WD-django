from django.contrib import admin, auth

# Register your models here.

from .models import *


class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'birthdate']


class CourseAdmin(admin.ModelAdmin):
    fields = ['topic', 'max_participants']


class MarkAdmin(admin.ModelAdmin):
    fields = ['value', 'comment', 'first_try']


class ParticipantListAdmin(admin.ModelAdmin):
    fields = ['course', 'student', 'mark']


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(ParticipantList, ParticipantListAdmin)
