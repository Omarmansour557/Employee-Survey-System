from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin  
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from employee.models import Employee
from employee.serializers import EmployeeSerializer, UserSerializer, PutEmployeeSerializer
from .models import Employee
# Create your views here.

class SignUpViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class =UserSerializer
    permission_classes = [AllowAny]

 
class EmployeeViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    @action(detail=False, methods= ['GET', 'PUT'] , permission_classes=[IsAuthenticated])
    def me(self, request):
        (employee, created) = Employee.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
            
        elif  request.method == 'PUT':
            if request.data.get('parent') or request.data.get('children'):
                return Response('Cannot edit parent or child. ')
            print(request.data)
            serializer = PutEmployeeSerializer(employee, data=request.data) 
            serializer.is_valid(raise_exception=True)  
            serializer.save()
            return Response(serializer.data)


   