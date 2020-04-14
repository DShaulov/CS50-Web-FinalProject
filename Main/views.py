from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

def index(reqeust):
    return render(reqeust, 'index.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    if request.method == "POST":
        username = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')

def login(request):
    return render(request, 'login.html')

