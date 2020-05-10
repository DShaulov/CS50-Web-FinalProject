"""Valdivian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('register', include('store.urls')),
    path('login', include('store.urls')),
    path('check_if_user_exists', include('store.urls')),
    path('logout', include('store.urls')),
    path('book-section', include('store.urls')),
    path('write-csv-to-database', include('store.urls')),
    path('electronics-section', include('store.urls'))
]
