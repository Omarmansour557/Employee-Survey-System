"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
import debug_toolbar
from survey_system.web_views import employee_survey_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.web_urls')),
    path('employee/', include('employee.web_urls')),

    path('api/employee/', include('employee.urls')) ,
    path("api/survey/", include('survey_system.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', employee_survey_list_view, name='home'),
    path('__debug__/', include(debug_toolbar.urls)),

]