from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse("contato 3 ")

def sobre(request):
    return HttpResponse("sobre 3 ")