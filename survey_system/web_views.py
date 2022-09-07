from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from employee.models import Employee
from django.contrib.auth.decorators import login_required

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
