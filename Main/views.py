from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

def index(reqeust):
    return render(reqeust, 'index.html')
