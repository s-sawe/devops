from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

def get_product(request, product_id):
    try:
        product = Product.objects.values().get(id=product_id)
        return JsonResponse(product)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

