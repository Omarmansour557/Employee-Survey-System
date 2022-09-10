
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Survey, EmployeeSurvey
from .serializers import AnswerSerializer, SurveySerializer, EmployeeSurveySerializer, QuestionSerializer
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

    @action(detail=True, methods= ['GET', 'POST'] , permission_classes=[AllowAny])
    def func(self, request, pk): 
        # for reverse
        for employee in Employee.objects.filter(employees__isnull = False).distinct():
               print(employee.name)
               print(employee.employees.all())
            #    for child in employee.employees.all():

            #         EmployeeSurvey.objects.create(rater=child, get_rated=employee, survey_id=1, is_submitted=False, submited_date='2022-02-06')

            #         print(employee.employees.all())
            # for followers
            # for employee in Employee.objects.filter(employees__isnull = False).distinct():
            #    print(employee.name)
            #    for child in employee.employees.all():

            #         EmployeeSurvey.objects.create(rater=employee, get_rated=child, survey_id=1, is_submitted=False, submited_date='2022-02-06')

            #    print(employee.employees.all())

            # return(Response('ok'))     

            # for employee in Employee.objects.all():
            #     print(employee.name)
            
            #     EmployeeSurvey.objects.create(rater=employee, survey_id=1, is_submitted=False, submited_date='2022-02-06')

            #     print(employee.employees.all()) 
        return(Response('ok')) 

class DemoViewSet( ViewSet,GenericViewSet):
        permission_classes = [AllowAny]
        @action(detail=True, methods= ['GET', 'POST'] , permission_classes=[AllowAny])
        def func(self, request, pk): 
            for employee in Employee.objects.filter(employees__isnull = False).distinct():
               print(employee.name)