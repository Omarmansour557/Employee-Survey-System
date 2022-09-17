from django.urls import path
from . import consumers
ws_urlpatterns = [
    path('ws/survey/', consumers.SurveyListConsumer.as_asgi()),
    path('ws/survey-detail/', consumers.SurveyDetailConsumer.as_asgi())
]