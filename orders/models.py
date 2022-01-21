from django.db import models

from django.core.validators import MinLengthValidator
import datetime
from Menu.models import MenuObj
from Authentication.models import Client
#from review.models import Review

unPreparedOrders = 0


class Order(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    menuObjs = models.CharField(max_length=2000,null=True)
    quatities = models.CharField(max_length=2000, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    alreadyPrepared = models.BooleanField(default=False)
    paymentMethod = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.client.user.username

