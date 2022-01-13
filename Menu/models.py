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
    morning = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    evning = models.BooleanField(default=False)
    outside = models.BooleanField(default=False)
    inside = models.BooleanField(default=False)
    category = models.ManyToManyField(categoryMenu)

    def __str__(self):
        return self.name
