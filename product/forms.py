from django import forms
from django.forms import ModelForm

from company.models import Company
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["sku",
                  "product_name",
                  "unit_of_measurement",
                  "price",
                  "supplier",
                  "manufacturer",
                  "product_category",
                  "discount",
                  "stock",
                  "description",
                  "photo",
                  ]


class SearchSortFilterForm(forms.Form):
    CHOICES = [
        ('more', 'Больше'),
        ('less', 'Меньше'),
    ]

    stock = forms.ChoiceField(
        choices=CHOICES,
        initial='more',
        required=False,
        label="Количество на складе"
    )

    search = forms.CharField(required=False,
                             label="Поиск")

    supplier = forms.ModelChoiceField(queryset=Company.objects.all(),
                                      empty_label="Все поставщики",
                                      required=False,
                                      label="Поставщик")