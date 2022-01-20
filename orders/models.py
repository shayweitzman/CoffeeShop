from django.db import models

from django.core.validators import MinLengthValidator
import datetime
from Menu.models import MenuObj
from Authentication.models import Client
#from review.models import Review

unPreparedOrders = 0


class Order(models.Model):
    client=models.OneToOneField(Client, on_delete=models.CASCADE)
    menuObjs = models.ManyToManyField(MenuObj,null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    alreadyPrepared = models.BooleanField(default=False)
    def __str__(self):
        return self.client.user.username

