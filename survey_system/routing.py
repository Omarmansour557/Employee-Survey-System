from django.urls import path
from . import consumers
ws_urlpatterns = [
    path('ws/survey/', consumers.SurveyConsumer.as_asgi())
]