from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    grade = models.CharField(max_length=4, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.grade
    
class SchoolData(models.Model):
    school_username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="school_user")
    is_school = models.BooleanField(default=True)
    school_name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.school_name
    

class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student_user')
    student_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='student_grade', null=True, to_field="grade")
    is_student = models.BooleanField(default=True)
    student_school = models.ForeignKey(SchoolData, on_delete=models.CASCADE, related_name='student_school', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_user.get_full_name()
    
    @property
    def school_name(self):
        return self.student_school.school_name
    
    @property
    def grade (self):
        return self.student_grade.grade
    
    
    