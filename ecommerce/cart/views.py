from django.contrib.messages.storage import session
from django.shortcuts import render, redirect, get_object_or_404

from ecommerceapp.models import product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    print(cart)
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, pk):
    print(pk)
    products = product.objects.get(id=pk)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print("i get the cart")
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))

        cart.save()
    #
    try:
        cart_item = CartItem.objects.get(products=products, cart__cart_id=_cart_id(request))
        if cart_item.quantity < cart_item.products.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            products=products,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        # print(cart.count)

        cart_items = CartItem.objects.filter(cart=cart, active=True)
        print(cart)

        print(cart_items)
        if cart_items is not None:
            for cart_item in cart_items:
                total += (cart_item.products.price * cart_item.quantity)
                counter += cart_item.quantity
        else:
            total = 0
            counter = 0
    except ObjectDoesNotExist:
        pass
    context = {
        "cart_items": cart_items,
        "total": total,
        "counter": counter
    }
    return render(request, 'cart.html', context)


def cart_remove(request, pk):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=pk)
    cart_item = CartItem.objects.get(products=products, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def cart_delete(request, pk):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=pk)
    cart_item = CartItem.objects.get(products=products, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
