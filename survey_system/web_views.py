from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Answer
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from survey_system.models import EmployeeSurvey
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@login_required()
def employee_survey_list_view(request):
    
    template_name = 'survey_list.html'
    user = request.user

    if user.is_staff:
        return redirect('admin:index')
    elif user.is_anonymous:
        return redirect('login')

    today = datetime.now()

    order_by = request.GET.get('order', '')
    page = request.GET.get('page', 1)
    reverse = request.GET.get('reverse', '')

    print(order_by)

    if order_by:
        if order_by == 'is_submitted':
            queryset = user.employee.survey_set.filter(survey__start_date__lte=today).order_by(f"{reverse}{order_by}")
        elif order_by == 'is_expired':
            queryset = sorted(user.employee.survey_set.filter(survey__start_date__lte=today), key = lambda emp_survey: emp_survey.survey.is_expired ,reverse=bool(reverse))
            print(queryset)
        else:
            queryset = user.employee.survey_set.filter(survey__start_date__lte=today).order_by(f"{reverse}survey__{order_by}")
    else:
        queryset = user.employee.survey_set.filter(survey__start_date__lte=today)
    


    paginator = Paginator(queryset, 5)

    context={
        'order_by':order_by,
        'employee_survey_list': paginator.page(page).object_list,
        'page_obj':paginator.page(page),
        'reverse':reverse
    }

    return render(request, template_name, context)

@login_required
def employee_survey_detail_view(request, pk):
    model = EmployeeSurvey
    template_name='survey_detail.html'
    context_object_name = 'employee_survey'

    if (request.user == model.objects.get(pk=pk).rater.user) or (request.user.is_staff):

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
            ws_coonsumer_answers = []

            if employee_survey.answers.all():
                for old_answer, new_answer in zip(employee_survey.answers.all(), answers):
                    old_answer.rating = new_answer
                    old_answer.save()
                    ws_coonsumer_answers.append(new_answer)
            else:
                for question, answer in zip(questions, answers):
                    answer = Answer(question=question, rating=answer)
                    answer.save()
                    employee_survey.answers.add(answer)
                    ws_coonsumer_answers.append(answer.rating)

            employee_survey.is_submitted = True
            employee_survey.save()

            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)('survey-detail',
            {
                'type':'new_answers',
                'status':'submitted',
                'answers':ws_coonsumer_answers
            }
            )
            return redirect('survey_detail', pk)

    else:
        raise PermissionDenied()