from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction

from tags.models import TaggedItem

from store.models import Collection, Product, Customer, Order, OrderItem, CartItem, Cart





def say_hello(request):

    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.unit_price = 10
        item.quantity = 1
        item.save()

    
    return render(request, 'hello.html', {'name': 'Mosh',})
