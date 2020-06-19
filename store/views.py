from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import User, Book, Laptop, Product, ProductCounter, Cart
import csv
import json
import math
import random

# Create your views here.


def index(request):
    try:
        user = User.objects.get(
            username = request.session['user']
        )
        user_first_name = user.first_name

        context = {
            'user': request.session['user'],
            'cart_count': request.session['cart_product_count'],
            'user_first_name': user_first_name,
            'current_page': 'index',
        }
    except KeyError:
        context = {
            'user': '',
            'cart_count': request.session['cart_product_count'],
            'current_page': 'index',
        }

    return render(request, 'index.html', context=context)


def register(request):
    if request.method == "GET":
        context = {
            'user': '',
            'cart_count': request.session['cart_product_count'],
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

        # Create a new cart for the user
        new_cart = Cart(
            user = new_user
        )
        new_cart.save()
        # Add all the products in the temporary cart to the permanent cart, if there are any
        try:
            all_products_ids = request.session['temp_product_cart']
            iterated_ids = []
            for id in all_products_ids:
                # get the product from the db
                product = Product.objects.get(
                        id = id
                    )

                # if product already exists in cart, increment the cart counter
                if id in iterated_ids:
                    product_counter = ProductCounter.objects.get(
                        cart = new_cart,
                        product = product
                    )
                    product_counter.product_count = product_counter.product_count + 1
                    product_counter.save()

                # if product does not exist
                else:
                    new_cart.products.add(product)

                    # add the product id to the list of iterated id's
                    iterated_ids.append(id)

                    # create a counter for the new product
                    new_counter = ProductCounter(
                        cart = new_cart,
                        product = product,
                        product_count = 1
                    )
                    new_counter.save()

            # once finished, delete the temporary cart
            del request.session['temp_product_cart']
        except KeyError:
            pass

        

        # Log the user in once he is registered
        request.session["user"] = username
        return HttpResponseRedirect("/")


def login(request):
    if request.method == "GET":
        context = {
            'user': '',
            'cart_count': request.session['cart_product_count'],
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
                'cart_count': request.session['cart_product_count'],
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
            'cart_count': request.session['cart_product_count'],
            'current_page': 'book-section',
            'books': Book.objects.all()
        }
        return render(request, 'book-section.html', context=context)
    except KeyError:
        context = {
            'user': '',
            'cart_count': request.session['cart_product_count'],
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
                generic_image_path='/static/media/book-icon.svg'
            )

            new_book.save()

    return HttpResponse(status=204)

def electronics_section(request):
    if request.method == "GET":
        try:
            context = {
            'user': request.session['user'],
            'cart_count': request.session['cart_product_count'],
            'current_page': 'electronics-section',
            'laptops': Laptop.objects.all()
        }

        except:
            context = {
            'user': '',
            'cart_count': request.session['cart_product_count'],
            'current_page': 'electronics-section',
            'laptops': Laptop.objects.all()
        }
        return render(request, 'electronics-section.html', context=context)

def electronics_product_page(request):
    if request.method == "POST":
        # Get the laptop from the database
        product_type = request.POST.get("product_type")
        product_name = request.POST.get("product_name")

        # Choose which database to search based on the product type
        if product_type == "Laptop":
            product = Laptop.objects.get(
                name = product_name
            )

        technical_details = product.technical_details
        technical_details_formatted = {}
        container = ""
        for letter in technical_details:
            if letter == '\n':
                container = container.replace('\r', '')
                key = container.split("\t")[0]
                value = container.split("\t")[1]
                technical_details_formatted[key] = value
                container = ""
                continue

            container = container + letter

        try:
            context = {
                'user': request.session['user'],
                'cart_count': request.session['cart_product_count'],
                'current_page' : "electronics-product-page",
                'product' : product,
                'technical_details': technical_details_formatted
            }

        except KeyError:
            context = {
                'user': '',
                'cart_count': request.session['cart_product_count'],
                'current_page' : "electronics-product-page",
                'product' : product,
                'technical_details': technical_details_formatted
            }

    
        return render(request, "electronics-product-page.html", context=context)


def book_product_page(request):
    if request.method == "POST":
        book_isbn = request.POST.get('book_isbn')
        
        book = Book.objects.get(
            isbn = book_isbn
        )

        try:
            context = {
                'user': request.session['user'],
                'cart_count': request.session['cart_product_count'],
                'current_page' : "book-product-page",
                'book' : book
            }

        except KeyError:
            context = {
                'user': '',
                'cart_count': request.session['cart_product_count'],
                'current_page' : "book-product-page",
                'book' : book
            }


        return render(request, "book-product-page.html", context=context)

def delete_duplicates(reqeust):
    duplicate_books = Book.objects.filter(
        isbn = "Flowing text, Google-generated PDF"
    )

    duplicate_books.delete()

            
    return HttpResponseRedirect("/")

def update_product_database(request):
    # get all the products and delete them
    all_products = Product.objects.all()
    all_products.delete()

    # add new products from each table
    all_laptops = Laptop.objects.all()
    all_books = Book.objects.all()


    for laptop in all_laptops:
        laptop_product = Product(
            name = laptop.name,
            price = laptop.price,
            type = "Laptop",
            average_rating = laptop.average_rating,
            review_count = laptop.review_count,
            generic_image_path = laptop.generic_image_path,
            product_image_path = laptop.product_image_path
        )
        laptop_product.save()

    for book in all_books: 
        book_product = Product(
            name = book.name,
            price = book.price,
            type = "Book",
            average_rating = book.average_rating,
            review_count = book.review_count,
            generic_image_path = book.generic_image_path,
            product_image_path = book.product_image_path
        )

        book_product.save()

    return HttpResponseRedirect("/")

def search_results(request):
    if request.method == "POST":
        search_text = request.POST.get('search-text')

        search_results_laptops_name = Laptop.objects.filter(name__contains=search_text)
        search_results_books_name = Book.objects.filter(name__contains=search_text)
        search_results_books_author = Book.objects.filter(author__contains=search_text)

       

        try:
            context = {
                'user': request.session['user'],
                'cart_count': request.session['cart_product_count'],
                'current_page' : "search-results",
                'search_results_laptops_name': search_results_laptops_name,
                'search_results_books_name': search_results_books_name,
                'search_results_books_author': search_results_books_author
            }

        except KeyError:
            context = {
                'user': '',
                'cart_count': request.session['cart_product_count'],
                'current_page' : "search-results",
                'search_results_laptops_name': search_results_laptops_name,
                'search_results_books_name': search_results_books_name,
                'search_results_books_author': search_results_books_author
            }
        return render(request, "search-results.html", context=context)


def add_to_cart(request):
    product_name = request.POST.get('product_name')
    product_type = request.POST.get('product_type')
    # get the product from the database
    product = Product.objects.get(
        name = product_name
    )
    

    # if its an existing user, get his cart and add the item to it
    try:
        user_object = User.objects.get(
            username = request.session['user']
        )
        user_cart = Cart.objects.get(
            user = user_object
        )
        user_cart.products.add(product)
        # check if a counter already exists for this product in this cart
        try:
            existing_counter = ProductCounter.objects.get(
                cart = user_cart,
                product = product
            )
            # if it exists, increment the amount by one

            existing_counter.product_count = existing_counter.product_count + 1
            existing_counter.save()
        except:
            # if an existing counter is not a found, create a counter for the product
            new_counter = ProductCounter(
                cart = user_cart,
                product = product,
                product_count = 1
            )
            new_counter.save()

    # if its not an existing user, add the products id to his request.session['temp_product_cart']
    except:
        # if its not his first product, add it to the existing dictionary
        try:
            request.session['temp_product_cart'].append(product.id)
            request.session.modified = True
        except KeyError:
            request.session['temp_product_cart'] = []
            request.session['temp_product_cart'].append(product.id)

    return HttpResponse('')

def cart_page(request):
    # If user has his own cart, get it
    try:
        user = User.objects.get(
            username = request.session['user']
        )
        cart_object = Cart.objects.get(
            user = user
        )
        all_products = []

        # arrange all the products inside a list
        for product in cart_object.products.all():
            # get the product count of the product
            product_counter = ProductCounter.objects.get(
                cart = cart_object,
                product = product
            )

            # create a new counter field for the product
            product.amount = product_counter.product_count
            all_products.append(product)

        context = {
            'user': request.session['user'],
            'cart_count': request.session['cart_product_count'],
            'current_page' : "cart-page",
            'cart': all_products
        }


    # If user does not have his own cart, get his temporary cart from request.session
    except KeyError:
        # see if user has a  temporary cart
        try:
            all_products = []
            iterated_ids = []
            temp_product_id_list = request.session['temp_product_cart']
            for id in temp_product_id_list:
                # if product was already iterated, continue to next iteration
                if id in iterated_ids:
                    continue

                # get the product from the database
                new_product = Product.objects.get(
                        id = id
                    )
                
                # see how many times the product id appears in the temp_product_id_list
                repeats = 0
                for element in temp_product_id_list:
                    if element == id:
                        repeats = repeats + 1
                # add the number of repeats to his request.session
                try:
                    # if he has an existing product_amount counter, append to it
                    request.session['product_amount'].append(repeats)
                    request.session.modified = True

                except:
                    # if he doesnt have an existing product_amount counter, create it and append to it

                    request.session['product_amount'] = []
                    request.session['product_amount'].append(repeats)
                    request.session.modified = True

                # add each product in his temp cart
                all_products.append(new_product)
                # add the product id to the iterated id's list
                iterated_ids.append(id)

            
            # associate each product with his own counter
            for index, product in enumerate(all_products):
                product.amount = request.session['product_amount'][index]


            # delete the request.session['product_amount] so as to not cause future error 
            del request.session['product_amount']
            context = {
                'user': '',
                'current_page' : "cart-page",
                'cart': all_products,
            }

            
        # if he doesnt have a cart
        except KeyError:
            context = {
                'user': '',
                'cart_count': request.session['cart_product_count'],
                'current_page' : "cart-page"
            }
    return render(request, "cart-page.html", context=context)

def checkout(request):
    # if its a registered user, checkout
    if 'user' in request.session:
        return HttpResponse('working on it')
    # if its not an existing user, redirect him to the register page
    else:
        return HttpResponseRedirect('/register')