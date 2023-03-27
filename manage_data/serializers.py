from rest_framework import serializers
from django.contrib.auth.models import User
from manage_data.models import *

      
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolData
        fields = ['school_name', 'city', 'pincode']
        
class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = ['student_grade', 'is_student', 'school_name']
        
class StudentUserSerializer(serializers.ModelSerializer):
    student_user = StudentSerializer(many=False, read_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'student_user']
        
    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        
        Student.objects.create(student_user=user, student_grade = validated_data['student_user']['student_grade'], school_name=validated_data['student_user']['school_name'])
        
        return user
        
        
class SchoolUserSerializer(serializers.ModelSerializer):
    school_user = SchoolSerializer(many=False)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'school_user']
        
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
    def create(self, validated_data):
                
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        user = User.objects.create(username=username, email=email, is_staff=True)
        user.set_password(password)
        user.save()
        
        SchoolData.objects.create(school_username = user, school_name = validated_data['school_user']['school_name'], city = validated_data['school_user']['city'], pincode = validated_data['school_user']['pincode'])
            
        return user
        
        
        
        
        
        
class AllUserSerializer(serializers.ModelSerializer):
    student_user = StudentSerializer(many=False, read_only = True)
    school_user = SchoolSerializer(many=False, read_only = True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'is_staff', 'student_user', 'school_user']
        
        
    
    