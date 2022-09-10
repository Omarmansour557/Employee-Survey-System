from .models import EmployeeSurvey, Survey
from employee.models import Employee
from django.dispatch import receiver
from django.db.models.signals import post_save
# dd/mm/YY


@receiver(post_save, sender=Survey)
def create_employe_survey(sender, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].survey_type == 'R':
                for employee in Employee.objects.filter(employees__isnull = False).distinct():
                    for child in employee.employees.all():
                            EmployeeSurvey.objects.create(rater=child, get_rated=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06' )
        elif kwargs['instance'].survey_type == 'F':

            for employee in Employee.objects.filter(employees__isnull = False).distinct():
               print(employee.name)
               for child in employee.employees.all():
                   EmployeeSurvey.objects.create(rater=employee, get_rated=child, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')
        elif kwargs['instance'].survey_type == 'G':
            for employee in Employee.objects.all():
                EmployeeSurvey.objects.create(rater=employee, survey_id=kwargs['instance'].id, is_submitted=False, submited_date='2022-02-06')