from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="loginview"),
    path('register/', views.register_view, name="registerview"),
    path('logout/', LogoutView.as_view(), name="logoutview"),
]