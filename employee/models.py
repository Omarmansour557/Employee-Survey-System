
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    job_title = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='employees')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')

    def __str__(self) -> str:
        return self.name

    @property
    def children(self):
        return self.employees.all()

    @property
    def url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})


    