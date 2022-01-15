from django.db import models
from django import forms

CATEGOTY_CHOICES = (
        ("7", "Salads"),
        ("8", "Meat"),
        ("9", "Dairy"),
        ("10", "Hot Drink"),
        ("11", "Cold Drink"),
        ("12", "Alcohol"),
    )

class categoryMenu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuObj(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='menu/images')
    availability = models.BooleanField(default=True)
    ageLimitation = models.BooleanField(default=False)
    VIP = models.BooleanField(default=False)
    morning = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    evning = models.BooleanField(default=True)
    outside = models.BooleanField(default=True)
    inside = models.BooleanField(default=True)
    drink = models.BooleanField(default=False)
    DOTD = models.BooleanField(default=False)
    category = models.ManyToManyField(categoryMenu)
    bought = models.IntegerField(default=0)


    def __str__(self):
        return self.name
