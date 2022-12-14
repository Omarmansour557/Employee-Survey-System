
from django.urls import path
from . import web_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', web_views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
