from django.shortcuts import render
from django.http import HttpResponse


def register_view(request):
    return HttpResponse("Essa é a tela de Register")

