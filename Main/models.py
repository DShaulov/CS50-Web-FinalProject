from django.db import models

# Create your models here.
class User(models.Model):
    """inbar ha gever"""
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
