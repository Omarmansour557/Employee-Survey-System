from time import sleep
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import EmployeeSurvey, Survey
from employee.models import Employee


@shared_task()
def notify_employees(message):
    print('Sending Surveys....')
    print(message)
    sleep(10)
    print('Surveys were successfully launched!')

@shared_task()
def launch_sruvey(**kwargs):
    channel_layer = get_channel_layer()
    consumer_data = []
    instance = Survey.objects.get(id=kwargs['id'])
    kwargs['instance'] = instance
    if kwargs['instance'].survey_type == 'R':
        for employee in Employee.objects.filter(employees__isnull = False).distinct():
            for child in employee.employees.all():
                    employee_survey = EmployeeSurvey.objects.create(rater=child, get_rated=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06' )
                    consumer_data.append(employee_survey.id)
    elif kwargs['instance'].survey_type == 'F':

        for employee in Employee.objects.filter(employees__isnull = False).distinct():
            for child in employee.employees.all():
                employee_survey = EmployeeSurvey.objects.create(rater=employee, get_rated=child, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')
                consumer_data.append(employee_survey.id)
    elif kwargs['instance'].survey_type == 'G':
        for employee in Employee.objects.all():
            employee_survey  = EmployeeSurvey.objects.create(rater=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')
            consumer_data.append(employee_survey.id)
    print('sending consumer data', consumer_data)
    async_to_sync(channel_layer.group_send)('survey',
    {
        'type':'new_survey',
        'new_surveys':consumer_data
    }
    )
