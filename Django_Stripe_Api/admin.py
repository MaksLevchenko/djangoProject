from django.contrib import admin

from Django_Stripe_Api.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


