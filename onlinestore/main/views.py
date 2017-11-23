from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from catalog.models import *
def home_page(request):
    featured=Product.objects.all()
    return render(request, 'home_page.html', {'featured':featured})

def detail_page(request, slug_):
    product=Product.objects.filter(slug=slug_)
    print(slug_)
    print(product.count())
    if product.count()<=0:
        return HttpResponseRedirect('/')
    return render(request, 'product_details.html', {'item':product[0]})

