
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Survey, EmployeeSurvey
from .serializers import AnswerSerializer, SurveySerializer, EmployeeSurveySerializer
from  employee.models import Employee
class SurveyViewSet(RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   CreateModelMixin,
                   GenericViewSet):
    # queryset = Answer.objects.all()
    serializer_class =EmployeeSurveySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        employee_object = self.request.user.employee    
        return employee_object.survey_set.all()

    @action(detail=True, methods= ['GET', 'POST'] , permission_classes=[IsAuthenticated])
    def SubmitAnswer(self, request, pk):
        if request.method == 'GET':
            employee_object = self.request.user.employee
            survey_employee = employee_object.survey_set.filter(id=pk)
            survey_id = survey_employee.values('survey')[0]['survey']
            survey_detail = Survey.objects.filter(id=survey_id)
            serializer = SurveySerializer(survey_detail, many=True)
        
            return Response(serializer.data)
        elif request.method =='POST':
            serializer = AnswerSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            answers = serializer.save()
            employee_survey = EmployeeSurvey.objects.get(pk=pk)
            survey_questions = employee_survey.survey.questions.all()
            for answer in answers:
                if answer.quetion not in survey_questions:
                    return Response({'errors': 'This Question No in This Survey '})
                employee_survey.answers.add(answer)
                employee_survey.save()
            return Response(serializer.data)