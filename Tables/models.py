from django.db import models
from Authentication.models import Client
from django.db.models.signals import post_save


class Tables(models.Model):
    number = models.IntegerField(unique=True)
    chairs = models.IntegerField(default=3)
    inside = models.BooleanField(default=True)

    def __str__(self):
        return str(self.number)


class Orders(models.Model):
    tables = models.OneToOneField(Tables, on_delete=models.CASCADE)
    clients = models.OneToOneField(Client, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
