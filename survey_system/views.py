from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from employee.serializers import EmployeeSerializer
from .models import Survey, EmployeeSurvey
from .serializers import SurveySerializer, EmployeeSurveySerializer
from  employee.models import Employee
# Create your views here.
from pprint import pprint
class SurveyViewSet(RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   GenericViewSet):
  
    serializer_class =EmployeeSurveySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        employee_object = self.request.user.employee
             
        return employee_object.survey_set.all()

    # @action(detail=False, methods= ['GET', 'PUT'] , permission_classes=[IsAuthenticated])
    # def me(self, request):

    #     if request.method == 'GET':
    #         serializer = EmployeeSurveySerializer(employee_surveys, many=True)
    #         return Response(serializer.data)

