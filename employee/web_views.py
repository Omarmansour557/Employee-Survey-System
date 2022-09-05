from django.shortcuts import render
from django.views.generic import DetailView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_detail.html'