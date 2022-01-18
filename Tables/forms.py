# from django import forms
# from django.forms import ModelForm
#
# from .models import Orders
#
#
# class DateInput(forms.DateInput):
#     input_type = 'date'
#
#
# class OrdersForm(ModelForm):
#
#     class Meta:
#         model = Orders
#         fields = ['tables', 'clients', 'date']
#         widgets = {
#             'date': DateInput(),
#         }