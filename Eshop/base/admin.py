from django.contrib import admin
# Register your models here.
from .models import Categories
from .models import Products
from .models import Posters

from .models import Wishlist
from .models import Cart



admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Posters)
admin.site.register(Wishlist)
admin.site.register(Cart)
