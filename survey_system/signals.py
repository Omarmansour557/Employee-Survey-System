from .models import EmployeeSurvey, Survey
from employee.models import Employee
from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .tasks import launch_sruvey
# dd/mm/YY


@receiver(post_save, sender=Survey)
def create_employe_survey(sender, instance, created, *args, **kwargs):
    print(kwargs)
    if created:
        launch_sruvey.apply_async(kwargs={'id':instance.id}, eta=instance.start_date)