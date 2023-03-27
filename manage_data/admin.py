from django.contrib import admin
from manage_data.models import *


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_username', 'school_name', 'city', 'pincode', 'created_at', 'updated_at' )

admin.site.register(SchoolData, SchoolAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_user', 'student_grade', 'student_school', 'created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)

admin.site.register(Grade)

