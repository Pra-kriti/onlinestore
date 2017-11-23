from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import *
from cart.models import *
from cart.views import _get_cart_items_count
import random

def home_page(request):
    items_cart=_get_cart_items_count(request)
    featured=Product.objects.all()
    return render(request, 'home_page.html', {'featured':featured, 'cart_count':items_cart})


