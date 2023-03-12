from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hello/index.html', {})


def greet(request, name:str):
    name = name.capitalize()
    return render(request, 'hello/greet.html', {'name':name})
