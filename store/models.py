from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.username}"



class Book(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    isbn = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    published_date = models.CharField(max_length=64)
    description = models.CharField(max_length=3600)
    publisher = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    generic_image_path = models.CharField(max_length=64)
    product_image_path = models.CharField(max_length=64, default="")
    review_count = models.CharField(max_length=64, default=0)
    average_rating = models.CharField(max_length=64, default=0)
    top_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.isbn}"

class Electronic(models.Model):
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=64)
    review_count = models.CharField(max_length=64)
    average_rating = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64, blank=True)
    top_seller = models.BooleanField(default=False)
    

class Laptop(Electronic):
    screen_size = models.CharField(max_length=64)
    generic_image_path = models.CharField(max_length=64)
    technical_details = models.TextField(blank=True)
    product_image_path = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    average_rating = models.CharField(max_length=64)
    review_count = models.CharField(max_length=64)
    generic_image_path = models.CharField(max_length=64, default="")
    product_image_path = models.CharField(max_length=64, default="")



    def __str__(self):
        return f"{self.name}, {self.type}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    products = models.ManyToManyField(Product)
    
class ProductCounter(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    product_count = models.IntegerField(default=1)


        
    
    
