from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from employee.models import Employee

class EmployeeCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    job_title = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields =  ('username', 'name', 'department', 'job_title', 'password1', 'password2')

    def save(self, commit = True):
        name = self.cleaned_data['name']
        department = self.cleaned_data['department']
        job_title = self.cleaned_data['job_title']
        employee = Employee(name=name, department=department, job_title =job_title)
        employee.user = self.instance
        self.instance.save()
        employee.save()
        return super().save(commit)
