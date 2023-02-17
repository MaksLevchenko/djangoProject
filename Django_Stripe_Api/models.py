from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_float_price(self):
        return "{0:.2f}".format(self.price / 100)
