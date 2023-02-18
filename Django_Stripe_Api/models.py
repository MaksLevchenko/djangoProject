from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username}'


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_float_price(self):
        return "{0:.2f}".format(self.price / 100)


