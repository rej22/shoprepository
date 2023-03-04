from django.shortcuts import render
from shop02.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if "q" in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(productName__contains = query ) | Q(productDescription__contains = query ))
    return render(request, 'search.html', {'query': query, 'products': products})
