from django.shortcuts import render, redirect
from django.contrib import messages
#from django.http import HttpResponse
from .models import Categories
from .models import Products
from .models import Posters
from .models import Wishlist
from .models import Cart

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

Categories_ = Categories.objects.all()
Products_ = Products.objects.all()
Posters_ = Posters.objects.all()
Wishlist_ = Wishlist.objects.all()
CartItems_ = Cart.objects.all()

# Create your views here.
def home(request):

    women_ID = 0
    men_ID = 0
    gadgets_ID = 0
    clothings_ID = 0
    supermarket_ID = 0

    # getting category ID's for the product
    for cat in Categories_:
        if cat.title == 'clothings':
            clothings_ID = cat.id

        if cat.title == 'gadgets':
            gadgets_ID = cat.id

        if cat.title == 'supermarket':
            supermarket_ID = cat.id
        

    
    return render(request, 'pages/featured.html', 
    {
        'allCategories': Categories_[:6],
        'allProducts': Products_[:5],
        'allPosters': Posters_,
        
        'kids': Products.objects.filter(kids_type=True)[:5],
        'gadgets': Products.objects.filter(category=gadgets_ID)[:5],
        'supermarket': Products.objects.filter(category=supermarket_ID)[:5],
        'topWomen': Products.objects.filter(gender='women')[:5],
        'topMen': Products.objects.filter(gender='men')[:5],
        'clothings': Products.objects.filter(category=clothings_ID)[:5],
        'featuredProducts': Products.objects.filter()[:3],
    }
    )

def categoryItems(request, title):
    
    return render(request, "pages/category.html",
    {
        'categoryName': title,
        'categoryProducts': Products_,
        'allCategories': Categories_,
        'allProducts': Products_,
        'wishlistItems': Wishlist_,
        'cartItems': CartItems_,
    }
    )


def men(request):
    menProducts = Products.objects.filter(gender='men')

    return render(request, "pages/men.html",
    {
        'allCategories': Categories_,
        'allProducts': Products_,
        'menProducts': menProducts,
    }
    )
    
def women(request):
    womenProducts = Products.objects.filter(gender='women')

    return render(request, "pages/women.html",
        {
        'allCategories': Categories_,
        'allProducts': Products_,
        'womenProducts': womenProducts,
    }
    )
    
def wishlist(request):

    return render(request, "pages/wishlist.html",
        {
        'allCategories': Categories_[:6],
        'allProducts': Products_[:5],
        'wishlistItems': Wishlist_,
    }
    )
    
def cart(request):
    return render(request, "pages/cart.html",
        {
        'allCategories': Categories_,
        'allProducts': Products_[:5],
        'allPosters': Posters_,
        'cartItems': CartItems_,
    }
    )
    
def product(request, id):
    item = {}
    relatedProducts = []

    for items in Products_:
        if (items.id == int(id)):
            item=items
            
            relatedProducts = Products.objects.filter(brand=item.brand, category=item.category)


    return render(request, "pages/product.html",
        {
        'allCategories': Categories_[:6],
        'allProducts': relatedProducts[:5],
        'allPosters': Posters_,
        'item':item,
        }
        )
    
def login(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "invalid Username!")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('men')
        else:
            messages.error(request, "invalid username or password!")

    return render(request, "pages/login.html",
        {
        'allCategories': Categories_,
        'allProducts': Products_,
        'allPosters': Posters_,
    }
    )


def logoutUser(request):
    logout(request)
    return redirect('/')

    
def register(request):
    return render(request, "pages/register.html",
        {
        'allCategories': Categories_,
        'allProducts': Products_,
        'allPosters': Posters_,
    }
    )

def addcart(request, id):
    return redirect('/product/'+str(id))

@login_required(login_url="login")
def addwishlist(request, id):
    return redirect('/product/'+str(id))

@login_required(login_url="login")
def dashboard(request):
    return render(request)
