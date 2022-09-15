from .models import EmployeeSurvey, Survey
from employee.models import Employee
from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# dd/mm/YY


@receiver(post_save, sender=Survey)
def create_employe_survey(sender, **kwargs):
    if kwargs['created']:
        channel_layer = get_channel_layer()
        consumer_data = []
        if kwargs['instance'].survey_type == 'R':
            for employee in Employee.objects.filter(employees__isnull = False).distinct():
                for child in employee.employees.all():
                        employee_survey = EmployeeSurvey.objects.create(rater=child, get_rated=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06' )
                        consumer_data.append(employee_survey)
        elif kwargs['instance'].survey_type == 'F':

            for employee in Employee.objects.filter(employees__isnull = False).distinct():
               for child in employee.employees.all():
                   employee_survey = EmployeeSurvey.objects.create(rater=employee, get_rated=child, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')
                   consumer_data.append(employee_survey)
        elif kwargs['instance'].survey_type == 'G':
            for employee in Employee.objects.all():
                employee_survey  = EmployeeSurvey.objects.create(rater=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')
                consumer_data.append(employee_survey)
        print('sending consumer data')
        async_to_sync(channel_layer.group_send)('survey',
        {
            'type':'new_survey',
            'new_surveys':consumer_data
        }
        )
