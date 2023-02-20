from django.contrib import admin

from Django_Stripe_Api.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_float_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_all_product_price')
