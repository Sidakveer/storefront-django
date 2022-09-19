from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection

from tags.models import TaggedItem

from store.models import Collection, Product, Customer, Order, OrderItem, CartItem, Cart





def say_hello(request):

    queryset = Product.objects.raw("SELECT * FROM store_product")

    # with connection.cursor as cursor:
    #     cursor.execute()

    
    return render(request, 'hello.html', {'name': 'Mosh',})
