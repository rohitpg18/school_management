from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from manage_data.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class StudentUserView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def get (self, request, *args, **kwargs):
        
        if request.user.id is None:
            
            return Response("You are not authorised to access this page")
        
        # admin can view all the registered students 
        elif request.user.username == 'admin':
            
            students = User.objects.filter(is_staff = False, student_user__is_student = True)

            serializer = StudentUserSerializer(students, many=True)

            return Response ({"All Students List":serializer.data})
        
        # if user is logged in as school students list of that school will be shown
        elif request.user.is_staff == True and request.user.school_user.is_school == True:

            school_name = request.user.school_user.school_name

            students = User.objects.filter(is_staff = False, student_user__student_school__school_name = school_name)

            serializer = StudentUserSerializer(students, many=True)

            return Response ({f"Students List of {school_name}":serializer.data})
        
        elif request.user.is_staff == False and request.user.student_user.is_student == True:
            
            students = User.objects.filter(is_staff = False, username = request.user.username)
            
            serializer = StudentUserSerializer(students, many=True)
            
            return Response ({"My Profile":serializer.data})
        
        
    
    
class SchoolUserView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def get (self, request, *args, **kwargs):

        if request.user.id is None:
            
            return Response("You are not authorised to access this page")
        
        # if user is logged in as admin all schools data will be shown
        elif request.user.username == 'admin':
            
            school = User.objects.filter(is_staff = True, school_user__is_school = True)

            serializer = SchoolUserSerializer(school, many=True)

            return Response ({"All Schools Data":serializer.data})
        
        # if looged in as school only their data will be shown
        if request.user.is_staff == True:
        
            school = User.objects.filter(is_staff=True, school_user__is_school = True, username = request.user.username)

            serializer = SchoolUserSerializer(school, many=True)

            return Response ({"School Profile":serializer.data})
        
        else:
            
            return Response("You have not authority to access this page")
        
        
    def post (self, request, format=None):
        
        if request.user.username == 'admin':
        
            serializer = SchoolUserSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()

                return Response (serializer.data)

            return Response (serializer.errors)
        
        else:
            return Response ("You dont have permission to create school acccount")
        
    
class AllUserView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def get (self, request, *args, **kwargs):
        
        if request.user.id is None:
            
            return Response("You are not authorised to access this page")
        
        # admin is able to view all users schools as well as students
        elif request.user.username == "admin":
            users = User.objects.all()

            serializer = AllUserSerializer(users, many=True)

            return Response({"All Users Data of Schools and Students":serializer.data})
        
        else:
            
            return Response("You have not authority to access this page")
        
    
    
        
        
        




    
