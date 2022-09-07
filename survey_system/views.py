from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Survey
from .serializers import SurveySerializer

# Create your views here.
class SurveyViewSet( RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   GenericViewSet):


 queryset = Survey.objects.all()                  
 serializer_class = SurveySerializer
 permission_classes = [IsAuthenticated]
 pagination_class = PageNumberPagination

