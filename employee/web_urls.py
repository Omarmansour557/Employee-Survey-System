
from django.urls import path
from . import web_views

urlpatterns = [
    path('', web_views.EmployeeListView.as_view(), name='employee_list'),
    path('<int:pk>/', web_views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('edit/<int:pk>/', web_views.EmployeeUpdateView.as_view(), name='employee_update')
]
