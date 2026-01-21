from decimal import Decimal, ROUND_HALF_UP

from django.contrib import messages
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django_resized import ResizedImageField

from company.models import Company


class Product(models.Model):
    # SELECT setval('product_product_id_seq', (SELECT MAX(id) FROM product_product));
    PRODUCT_NAME_CHOICES = [("Ботинки","Ботинки"),
                    ("Кеды","Кеды"),
                    ("Кроссовки","Кроссовки"),
                    ("Полуботинки","Полуботинки"),
                    ("Сапоги","Сапоги"),
                    ("Тапочки","Тапочки"),
                    ("Туфли","Туфли"),
                    ]
    UNIT_OF_MEASUREMENT_CHOICES = [("шт.", "шт.")]

    PRODUCT_CATEGORY_CHOICES = [("Женская обувь", "Женская обувь"),
                                   ("Мужская обувь", "Мужская обувь")]

    sku = models.CharField(max_length=120,
                           verbose_name="Артикул",)
    product_name = models.CharField(max_length=120,
                                    choices=PRODUCT_NAME_CHOICES,
                                    verbose_name="Наименование товара",)
    unit_of_measurement = models.CharField(max_length=20,
                                           choices=UNIT_OF_MEASUREMENT_CHOICES,
                                           verbose_name="Единица измерения",)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))],
                                verbose_name="Цена",)

    supplier = models.ForeignKey(Company,
                                 on_delete=models.CASCADE,
                                 related_name="suppliers",
                                 related_query_name="supplier",
                                 verbose_name="Поставщик",)
    manufacturer = models.ForeignKey(Company,
                                     on_delete=models.CASCADE,
                                     related_name="manufacturers",
                                     related_query_name="manufacturer",
                                     verbose_name="Производитель",)
    product_category = models.CharField(max_length=20,
                                        choices=PRODUCT_CATEGORY_CHOICES,
                                        verbose_name="Категория",)
    discount = models.DecimalField(max_digits=10,
                                   decimal_places=2,
                                   validators=[MinValueValidator(Decimal('0'))],
                                   verbose_name="Скидка",)
    stock = models.PositiveIntegerField(verbose_name="Количество на складе")
    description = models.CharField(max_length=400,
                                   verbose_name="Описание")
    photo = ResizedImageField(
        size=[300, 200],
        null=True,
        default='picture.png',
        verbose_name="Изображение",
    )


        # models.ImageField(null=True, default='picture.png')


    def get_price(self):
        result = "" + str(self.price) + " руб."

        if self.discount > 0:
            new_price = (self.price - self.price * (self.discount)/100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            result = "<span class='old-price'>" + str(self.price) + "</span> <span class='new-price'>" + str(new_price) + " руб. </span>"

        return result

    def __str__(self):
        return "" + str(self.pk) + ": " + self.product_name + ": " + self.description