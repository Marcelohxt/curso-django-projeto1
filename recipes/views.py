from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html',context={
        "name": "Receitas da Vovó Zuila"
        })


def contato(request):
    return HttpResponse("contato 3 ")

def sobre(request):
    return HttpResponse("sobre 3 ")