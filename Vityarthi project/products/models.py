from django.db import models


class Product(models.Model):
    Name=models.CharField(max_length=100)
    Price=models.FloatField()
    Stock=models.IntegerField()
    image_Url=models.CharField(max_length=2085)

class Offer(models.Model):
    code=models.CharField()
    description=models.CharField()
    discount=models.FloatField()





