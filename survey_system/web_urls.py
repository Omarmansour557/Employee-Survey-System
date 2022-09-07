
from django.urls import path
from . import web_views

urlpatterns = [
    path('<int:pk>', web_views.EmployeeSurveyDetailView.as_view(), name='survey_detail')
]
