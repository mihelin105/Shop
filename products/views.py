from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# click on the home button - /products -> call the index function
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse("New decor.")

def home(request):
    return render(request, 'home.html')

def decor_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'decor_list.html', {'products': products, 'category': category_name})