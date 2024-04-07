from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to = 'images/categories')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



## products Model

class Products(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    sport_headline = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    currency = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    offers_title = models.CharField(max_length=200)
    offers_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50)
    kids_type = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    ratings = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to = 'images/products')

    size = models.CharField(max_length=150)
    #wish = models.BooleanField()
    #cart = models.BooleanField()


    def __str__(self):
        return self.title


class Posters(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'images/posters')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product.title
