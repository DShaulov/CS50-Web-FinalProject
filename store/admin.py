from django.contrib import admin
from .models import User, Book, Laptop, Product, Cart, ProductCounter

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Laptop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductCounter)



