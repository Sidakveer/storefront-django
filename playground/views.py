from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType

from tags.models import TaggedItem

from store.models import Collection, Product, Customer, Order, OrderItem





def say_hello(request):

    collection = Collection.objects.get(pk=11)
    collection.featured_product = None
    collection.save()

    
    return render(request, 'hello.html', {'name': 'Mosh',})
