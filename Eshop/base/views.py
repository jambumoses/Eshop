from django.shortcuts import render
#from django.http import HttpResponse
#from .Model import Categories;



# Create your views here.
def home(request):
    #allCategories = Categories.object.all()
    return render(request, 'pages/featured.html')
    """ {'Categories': allCategories}) """
    
def men(request):
    return render(request, "pages/men.html")
    
def women(request):
    return render(request, "pages/women.html")
    
def wishlist(request):
    return render(request, "pages/wishlist.html")
    
def cart(request):
    return render(request, "pages/cart.html")
    
def product(request, id):
    return render(request, "pages/product.html")
    
def login(request):
    return render(request, "pages/login.html")
    
def register(request):
    return render(request, "pages/register.html")
