from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import datetime

#from book_catalog.models import Book
#from review.models import Review



class Barista(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=50,default='Barista')
    ordersToPrepare= models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class Client(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50,default='Client')
    Is_VIP = models.BooleanField(default=False,verbose_name='VIP Client?')
    birthday = models.DateField(default=datetime.date.today)
    coffeeCups = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
