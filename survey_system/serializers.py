from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['survey_type', 'end_date', 'start_date', 'description', 'title', 'questions']

