from django.db import models
from Authentication.models import Client
from django.db.models.signals import post_save



class Table(models.Model):
    number = models.IntegerField(unique=True)
    chairs = models.IntegerField(default=3)
    inside = models.BooleanField(default=True)
    Days_CHOICES = (
        ('', ''), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday')
    )
    UnavailabDay = models.CharField(default='', choices=Days_CHOICES, max_length=100)

    def __str__(self):
        return str(self.number)


class TableOrder(models.Model):
    tables = models.ForeignKey(Table, on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = ('tables', 'time', 'date')
