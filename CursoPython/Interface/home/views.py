from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def meu_metodo(request):
    return HttpResponse('Bom dia  Aula de Introdução')
