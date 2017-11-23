# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from cart.models import *
from cart.views import _get_cart_items_count, _generate_cart, _add_to_cart
from catalog.models import *

# Create your views here.
def detail_page(request, slug_):
    if request.POST:
        if request.session.get('cart_id','')=='':
            request.session['cart_id']=_generate_cart()

        # else:
            # return HttpResponseRedirect('www.google.com')
        _add_to_cart(request)

    items_cart = _get_cart_items_count(request)
    try:
        product=Product.objects.get(slug=slug_)
    except:
        return HttpResponseRedirect('/')
    return render(request, 'product_details.html', {'item':product, 'cart_count':items_cart})
