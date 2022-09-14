from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from store.models import Collection, Product, Customer, Order, OrderItem





def say_hello(request):

    # queryset = Customer.objects.all()
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Customer.objects.filter(email__icontains=".com")
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset = Order.objects.filter(customer__id=1)
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    




    

    return render(request, 'hello.html', {'name': 'Mosh', "products": list(queryset)})
