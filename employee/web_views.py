from django.shortcuts import render
from django.views.generic import DetailView
from .models import Employee

# Create your views here.

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'