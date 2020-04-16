from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('check_if_user_exists', views.check_if_user_exists, name="check_if_user_exists"),
    path('logout', views.logout, name='logout')
]