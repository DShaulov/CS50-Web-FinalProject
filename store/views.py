from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import User, Book, Laptop
import csv
import json
import math

# Create your views here.


def index(request):
    try:
        context = {
            'user': request.session['user'],
            'current_page': 'index',
        }
    except KeyError:
        context = {
            'user': '',
            'current_page': 'index',
        }

    return render(request, 'index.html', context=context)


def register(request):
    if request.method == "GET":
        context = {
            'user': '',
            'current_page': 'login/register'
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
            username=username,
            password=password_hash,
            first_name=first_name,
            last_name=last_name
        )

        new_user.save()

        # Log the user in once he is registered
        request.session["user"] = username
        return HttpResponseRedirect("/")


def login(request):
    if request.method == "GET":
        context = {
            'user': '',
            'current_page': 'login/register'
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
                'user': '',
                'error': '* Email or password incorrect',
                'current_page': 'login/register'
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


def book_section(request):
    try:
        context = {
            'user': request.session['user'],
            'current_page': 'book-section',
            'books': Book.objects.all()
        }
        return render(request, 'book-section.html', context=context)
    except KeyError:
        context = {
            'user': '',
            'current_page': 'book-section',
            'books': Book.objects.all()
        }
        return render(request, 'book-section.html', context=context)


def write_csv_to_database(request):
    with open('store/media/books-list.csv', 'r', errors='ignore') as file:
        csv_reader = csv.reader(file)
        pass_header = 1
        for entry in csv_reader:
            if pass_header == 1:
                pass_header = 0
                continue
            title = entry[1]
            author = entry[2]
            price = math.floor(float(entry[5]))
            description = entry[7]
            publisher = entry[8]
            genre = entry[10]
            isbn = entry[11]
            language = entry[12]
            published_date = entry[13]

            new_book = Book(
                isbn=isbn,
                title=title,
                price=price,
                description=description,
                author=author,
                published_date=published_date,
                genre=genre,
                language=language,
                publisher=publisher,
                image_path='/static/media/book-icon.svg'
            )

            new_book.save()

    return HttpResponse(status=204)

def electronics_section(request):
    if request.method == "GET":
        try:
            context = {
            'user': request.session['user'],
            'current_page': 'electronics-section',
            'laptops': Laptop.objects.all()
        }

        except:
            context = {
            'user': '',
            'current_page': 'electronics-section',
            'laptops': Laptop.objects.all()
        }
        return render(request, 'electronics-section.html', context=context)
