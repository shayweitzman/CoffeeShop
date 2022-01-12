from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Barista,Client
from django.forms.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date



class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2',)

    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class BaristaProfileForm(forms.ModelForm):
    class Meta:
        model=Barista
        fields = ()
class ClientProfileForm(forms.ModelForm):
    class Meta:
        model=Client
        fields= ('birthday','Is_VIP')
        widgets={
            'birthday':SelectDateWidget(years=range (1900, date.today().year+1)),
        }

