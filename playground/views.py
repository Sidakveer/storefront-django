from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum
from django.db.models.functions import Concat
from store.models import Collection, Product, Customer, Order, OrderItem





def say_hello(request):

    # queryset = Customer.objects.all()
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Customer.objects.filter(email__icontains=".com")
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset = Order.objects.filter(customer__id=1)
    # queryset = Product.objects.select_related("collection").all() # for one to many relationship
    # queryset = Product.objects.prefetch_related("promotion").all() # for many to many relationship
    # queryset = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    # orders = Order.objects.aggregate(count=Count("id"))
    # pr = OrderItem.objects.filter(product_id=1).aggregate(sum=Sum("quantity"))
    # cu = Order.objects.filter(customer_id=1).aggregate(sum=Sum("id"))
    # co = Product.objects.filter(collection_id=3).aggregate(max=Max("unit_price"), min=Min("unit_price"), avg=Avg("unit_price"))
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    #     )
    queryset = Customer.objects.annotate(
        orders_count=Count("order")
    )


    

    return render(request, 'hello.html', {'name': 'Mosh', "products": list(queryset)})
