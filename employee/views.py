from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin  
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class EmployeeViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer

    @action(detail=False)
    def me(self, request):
        employee = Employee.objects.get(user_id=request.user.id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)