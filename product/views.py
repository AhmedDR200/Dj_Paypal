from django.shortcuts import render
from .models import Product , Order
# Create your views here.


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, 'product/detail.html', {'product':product})