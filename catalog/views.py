from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product

def index(request):
    return HttpResponse("Catalog home page.")

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {
        'categories': categories
    })

def product_list(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {
        'products': products
    })
