from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User
import json

# Create your views here.

def index(request):
    try:
        context = {
            'user': request.session['user'],
            'current_page': 'index'
        }
    except KeyError:
        context = {
            'user': '',
            'current_page': 'index'
        }

    return render(request, 'index.html', context=context)


def register(request):
    if request.method == "GET":
        context = {
            'user': '',
            'current_page': 'register'
        }
        return render(request, 'register.html', context=context)

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

        # TODO log the user in once he is registered
        return render(request, 'index.html')

        

def login(request):
    if request.method == "GET":
        context = {
            'user': '',
            'current_page': 'login'
        }
        return render(request, 'login.html', context=context)

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        # check that user exists
        user_query_set = User.objects.filter(username=username)

        # if doesnt exist, return an error 
        if len(user_query_set) == 0:
            context = {
                'error': '* Email or password incorrect'
            }
            return render(request, 'login.html', context=context)

        else:
            # create a session entry for the current user
            request.session["user"] = user_query_set[0].username
            return HttpResponseRedirect(redirect_to='/')



def check_if_user_exists(request):
    email = request.POST.get('email')

    # search for the username in the database
    existing_user_queryset = User.objects.filter(username=email)

    # if queryset has zero results, no user exists
    if len(existing_user_queryset) == 0:
        return HttpResponse("No existing user")

    else:
        return HttpResponse("A user exists")

def logout(request):
    del request.session['user']
    return HttpResponseRedirect(redirect_to='/')


