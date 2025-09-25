from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse("Essa é a tela de Login")

def register_view(request):
    return HttpResponse("Essa é a tela de Register")

def logout_view(request):
    return HttpResponse("Essa é a tela de Logout")