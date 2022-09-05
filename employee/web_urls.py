
from django.urls import path
from . import web_views

urlpatterns = [
    path('<int:pk>/', web_views.EmployeeDetailView.as_view(), name='employee_profile'),
    path('edit/<int:pk>', web_views.EmployeeUpdateView.as_view(), name='employee_edit')
]
