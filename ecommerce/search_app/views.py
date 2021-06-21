from django.shortcuts import render
from ecommerceapp.models import product
from django.db.models import Q

# Create your views here.

def SearchResult(request):
    products = None
    query = None
    if "q" in request.GET:
        query = request.GET.get('q')
        products = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'SearchResult.html', {'query':query,'products':products})
