
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    job_title = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


