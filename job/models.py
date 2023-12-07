from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    productCode = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField()
    currency = models.CharField(max_length=3)
    qty = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
