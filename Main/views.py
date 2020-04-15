from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User
# Create your views here.

def index(reqeust):
    return render(reqeust, 'index.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    if request.method == "POST":
        username = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_hash = make_password(password=password)

        # Create a new user with the provided credentials
        new_user = User(
            username = username,
            password = password_hash,
            first_name = first_name,
            last_name = last_name            

        )

        new_user.save()
        return render(request, 'index.html')

        

def login(request):
    return render(request, 'login.html')

