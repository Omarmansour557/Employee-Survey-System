from dataclasses import field
from rest_framework import serializers
from .models import Answer, Survey , EmployeeSurvey, Questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'description']
class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Survey
        fields = ['id','survey_type', 'end_date', 'start_date', 'description', 'title', 'questions']

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['rating', 'quetion']
class EmployeeSurveySerializer(serializers.ModelSerializer):
    rater = serializers.StringRelatedField()
    get_rated = serializers.StringRelatedField()
    answers = AnswerSerializer(many=True)
    class Meta:
        model = EmployeeSurvey
        fields = ['is_submitted', 'rater', 'get_rated', 'survey', 'submited_date', 'answers']
