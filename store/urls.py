from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('check_if_user_exists', views.check_if_user_exists, name="check_if_user_exists"),
    path('logout', views.logout, name='logout'),
    path('book-section', views.book_section, name="book-section"),
    path('write-csv-to-database', views.write_csv_to_database, name="write-csv-to-database"),
    path('electronics-section', views.electronics_section, name="electronics-section"),
    path('electronics-product-page', views.electronics_product_page, name="electronics-product-page"),
    path('book-product-page', views.book_product_page, name="book-product-page"),
    path('delete-duplicates', views.delete_duplicates, name="delete-duplicates"),
    path('update-product-database', views.update_product_database, name="update-product-database"),
    path('search-results', views.search_results, name="search-results"),
    path('cart-page', views.cart_page, name="cart-page"),
    path('add-to-cart', views.add_to_cart, name="add-to-cart"),
    path('checkout', views.checkout, name="checkout")

]