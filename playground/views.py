from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType

from tags.models import TaggedItem

from store.models import Collection, Product, Customer, Order, OrderItem, CartItem, Cart





def say_hello(request):

    # cart = Cart()
    # cart.save()

    # cartitem = CartItem.objects.get(pk=2)
    # cartitem.quantity = 12
    # cartitem.cart = cart
    # cartitem.product_id = 1
    # cartitem.save()
    
    cart = Cart(pk=2)
    cart.delete()

    
    return render(request, 'hello.html', {'name': 'Mosh',})
