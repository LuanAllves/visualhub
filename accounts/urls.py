from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name="loginview"),
    path('register/', views.register_view, name="registerview"),
    path('logout/', views.logout_view, name="logoutview"),
]