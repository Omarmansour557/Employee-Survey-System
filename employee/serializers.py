
from rest_framework import serializers

from  .models import Employee
from django.contrib.auth.models import User
from survey_system.models import Questions, Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['survey_type', 'end_date', 'start_date', 'description', 'title', 'questions']

class ChildrenSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    children = ChildrenSeriallizer(many=True)
    parent = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department','children',  'job_title', 'parent']
class PutEmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department','job_title']
            
        
class UserSerializer(serializers.ModelSerializer):
    employee = PutEmployeeSerializer()
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}  
        fields = ('username', 'email', 'password','employee')

    def create(self, validated_data):

        # create user 
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            
            password = validated_data['password']
        )
        

        employee_data = validated_data.pop('employee')
        # create profile
        employee = Employee.objects.create(
            user = user,
            name = employee_data['name'],
            department = employee_data['department'],
            job_title = employee_data['job_title']
            
        )
        
        return UserSerializer(user).data
        # user.pop('password')
        # return user