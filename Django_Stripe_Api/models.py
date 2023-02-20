from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_float_price(self):
        return "{0:.2f}".format(self.price / 100)


class Order(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.username}'

    def get_all_product_price(self):
        return "{0:.2f}".format(sum(price.price for price in self.product.all())/100)
