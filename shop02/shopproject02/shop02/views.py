from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def allProductCategory(request, category_slug =None):
    category_page = None
    products_list = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products_list = Product.objects.all().filter(category = category_page, productAvailable= True)
    else:
        products_list = Product.objects.all().filter(productAvailable=True)
    paginator = Paginator(products_list, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': category_page, 'products': products})

def productDetail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
