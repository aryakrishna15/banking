from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_form(request):
    return render(request, 'register_form.html')
