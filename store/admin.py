from itertools import product
from math import prod
from django.contrib import admin
from . import models
from django.db.models.aggregates import Max, Min, Count ,Avg, Sum

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "inventory", "collection_title"]
    list_editable = ["unit_price"]

    @admin.display(ordering="inventory")
    def inventory_status(self,  product):
        if product.inventory < 10:
            return "Low"
        return "OK" 
    
    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10

admin.site.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]

    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count("product")
        )

    


