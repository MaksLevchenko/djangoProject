from django.contrib import admin

from Django_Stripe_Api.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
