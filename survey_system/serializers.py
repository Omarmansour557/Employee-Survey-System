from rest_framework import serializers
from .models import Survey , EmployeeSurvey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id','survey_type', 'end_date', 'start_date', 'description', 'title', 'questions']

class EmployeeSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSurvey
        fields = ['is_submitted', 'rater', 'get_rated', 'survey', 'submited_date', 'answers']