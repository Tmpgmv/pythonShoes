from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'delivery_date', 'office', 'status', ]
        widgets = {
            'order_date': forms.DateInput(format='%Y-%m-%d',
                                             attrs={'type': 'date'}),
            'delivery_date': forms.DateInput(format='%Y-%m-%d',
                                             attrs={'type': 'date'}),
        }