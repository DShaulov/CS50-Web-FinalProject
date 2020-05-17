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
    description = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    image_path = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Electronic(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    review_count = models.CharField(max_length=64)
    average_rating = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64, blank=True)
    

class Laptop(Electronic):
    screen_size = models.CharField(max_length=64)
    image_url = models.CharField(max_length=64)
    technical_details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.name}"
    
