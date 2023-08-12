from django.http import JsonResponse
from django.shortcuts import render
from .models import Product , Order
import json
# Create your views here.


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, 'product/detail.html', {'product':product})



def order_completed(request):
    body = json.loads(request.body)
    product = Product.objects.get(id=body['product_id'])
    Order.objects.create(
        product = product ,
        order_id = 312321312 ,
        order_completed = True
    )

    return JsonResponse('Payment Compeleted')

