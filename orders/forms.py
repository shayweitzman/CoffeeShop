from Tables.models import TableOrder
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TableOrderForm(forms.ModelForm):
    class Meta:
        model = TableOrder
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

