
from dataclasses import fields
from rest_framework import serializers

import employee
from  .models import Employee
from django.contrib.auth.models import User

class ChildrenSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    children = ChildrenSeriallizer(many=True)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department','children',  'job_title', 'parent']
class PutEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department','job_title']
            
        
class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password','employee')

    def create(self, validated_data):

        # create user 
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            employee = validated_data['employee'],
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

        return user