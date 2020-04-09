from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

def index(reqeust):
    return render(reqeust, 'index.html')


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')