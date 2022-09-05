
from django.urls import path
from . import web_views

urlpatterns = [
    path('<int:pk>/', web_views.EmployeeDetailView.as_view(), name='profile')
]
