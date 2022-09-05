
from django.urls import path
from . import web_views

urlpatterns = [
    path('signup/', web_views.SignUpView.as_view(), name='signup')
]
