from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# /product --> index
# URL (Uniform Resource Locator) --> Address


def index(request):

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


