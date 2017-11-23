# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from catalog.models import *
from cart.models import *


# Create your views here.
#Display Cart Page
def _cart_page(request):
    cart_items=_get_cart_items(request)
    return render(request, 'cart_page.html', {'cart':cart_items,'cart_count':cart_items.count()})


# If the user has not created cart id generate Cart ID for a Cart
def _generate_cart():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@  # $%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters) - 1)]
    return cart_id


# Adding product items to cart
def _add_to_cart(request):
    #get Post Data
    postdata=request.POST.copy()
    # Get Product Slug
    product_slug=postdata.get('product_slug','')
    #Fetch product or return missing page
    p=get_object_or_404(Product, slug=product_slug)
    # Check if the object is in the cart
    cart_items=_get_cart_items(request)
    product_in_cart=False
    for item in cart_items:
        if item.product.id==p.id:
            #Update the quantity for the cart_item
            item.augment_quantity(1)
            product_in_cart=True
    if not product_in_cart:
        item=CartItem()
        item.cart_id=request.session.get('cart_id')
        item.product=p
        item.quantity=1
        item.save()
        print("Cart_Item has been added")




# Get Items from the cart
def _get_cart_items(request):
    products=CartItem.objects.filter(cart_id=request.session.get('cart_id'))
    return products

# Count and return number of cart items
def _get_cart_items_count(request):
    items=_get_cart_items(request)
    count=0
    for item in items:
       count+=item.quantity
    return count


