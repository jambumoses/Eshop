from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('cart/', views.cart, name="cart"),
    path('product/<str:id>/', views.product, name="product"),
    path('category/', views.category_products, name="allproducts"),
    path('category/<str:title>/', views.categoryItems, name="category"),

    path('addwishlist/<str:id>/', views.addwishlist, name="addwishlist"),
    path('addcart/<str:id>/', views.addcart, name="addcart"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('spyder/', views.spyderView, name='spyder')
]