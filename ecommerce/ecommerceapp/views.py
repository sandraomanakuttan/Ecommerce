from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import category, product
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Create your views here.

def allProdCat(request, c_slug=None):
    global products
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        products_list = product.objects.filter(category=c_page, available=True)
    else:
        products_list = product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "category.html", {'category': c_page, 'products': products})


def ProdCatDetail(request, c_slug, product_slug):
    print(c_slug)
    try:
        products = product.objects.get(category__slug=c_slug, slug=product_slug)
        print(products)
    except Exception as e:
        products =""
        raise e
    # return HttpResponse(products)
    return render(request, "product.html", {'products': products})
