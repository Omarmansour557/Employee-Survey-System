
from django.urls import path
from . import web_views

urlpatterns = [
    path('<int:pk>/', web_views.employee_survey_detail_view, name='survey_detail')
]
