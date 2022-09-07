from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from employee.models import Employee
from django.contrib.auth.decorators import login_required
from .models import Answer

from survey_system.models import EmployeeSurvey


@login_required()
def employee_survey_list_view(request):
    template_name = 'survey_list.html'
    user = request.user

    
    if user.is_staff:
            return redirect('admin:index')
    elif user.is_anonymous:
        return redirect('login')

    context={
        'survey_list': user.employee.survey_set.all()
    }

    return render(request, template_name, context)
class EmployeeSurveyDetailView(DetailView):
    model = EmployeeSurvey
    template_name='survey_detail.html'
    context_object_name = 'employee_survey'

    def post(self, request, pk):
        # print(request.body)
        HttpResponse('ss')

def employee_survey_detail_view(request, pk):
    model = EmployeeSurvey
    template_name='survey_detail.html'
    context_object_name = 'employee_survey'

    if request.method == 'GET':
        context = {
            context_object_name: model.objects.get(pk=pk)
        }

        return render(request, template_name, context)
    
    elif request.method == 'POST':
        print(request.POST.getlist('answer'))
        employee_survey = model.objects.get(pk=pk)
        questions = employee_survey.survey.get_questions
        answers = request.POST.getlist('answer')
    
        for question, answer in zip(questions, answers):
            answer = Answer(question=question, rating=answer)
            answer.save()
            employee_survey.answers.add(answer)
        employee_survey.is_submitted = True
        employee_survey.save()

        return redirect('survey_detail', pk)
