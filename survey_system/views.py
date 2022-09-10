
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Survey, EmployeeSurvey
from .serializers import AnswerSerializer, SurveySerializer, EmployeeSurveySerializer, QuestionSerializer
from  employee.models import Employee
from .tasks import notify_employees
import datetime

today = datetime.date.today()


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
        if employee_object.surveys.filter(start_date__lte = today).distinct():
            print(employee_object.surveys.filter(start_date__lte = today).distinct())
            list_surveys = []
            for surveys in  employee_object.surveys.filter(start_date__lte = today).distinct():
                for employe_survy in employee_object.survey_set.filter(survey=surveys):
                    list_surveys.append(employe_survy)
            return list_surveys
      
        else:
            return EmployeeSurvey.objects.none()

    @action(detail=True, methods= ['GET', 'POST'] , permission_classes=[IsAuthenticated])
    def SubmitAnswer(self, request, pk):
        if request.method == 'GET':
            employee_survey = EmployeeSurvey.objects.get(pk=pk)
            questions = employee_survey.survey.questions.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        elif request.method =='POST':
            serializer = AnswerSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            answers = serializer.save()
            employee_survey = EmployeeSurvey.objects.get(pk=pk)
            survey_questions = employee_survey.survey.questions.all()
            for answer in answers:
                if answer.quetion not in survey_questions:
                    return Response({'errors': 'This Question Not in This Survey '})

                employee_survey.answers.add(answer)

            employee_survey.is_submitted = 'True'
            employee_survey.save()
            return Response(serializer.data)

class DemoViewSet(ModelViewSet):
        serializer_class = SurveySerializer
        queryset= Survey.objects.all()
        permission_classes = [AllowAny]
        @action(detail=True, methods= ['GET', 'POST'] , permission_classes=[AllowAny])
        def func(self, request, pk): 
            notify_employees.delay('Hello')
            return Response('ok')

            