from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('cart/', views.cart, name="cart"),
    path('product/<str:id>/', views.product, name="product"),

    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]