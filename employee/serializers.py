
from rest_framework import serializers
from  .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Employee
        fields = ['id', 'user_id','name', 'department', 'parent', 'job_title']
        
