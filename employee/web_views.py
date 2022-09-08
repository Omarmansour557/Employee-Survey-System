from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_list.html'
    paginate_by = 1

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class EmployeeUpdateView(UserPassesTestMixin, UpdateView):
    model = Employee
    template_name = 'employee_update.html'
    fields = ['name', 'department', 'job_title']

    def test_func(self):
        self.request.user == self.get_object().user
        return self.request.user == self.get_object().user