from django.db import models

from order.models import Order
from product.models import Product


class OrderProduct(models.Model):
    # SELECT setval('order_product_orderproduct_id_seq', (SELECT MAX(id) FROM order_product_orderproduct));
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                verbose_name="Товар")
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name="Заказ")
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 verbose_name="Количество")

    def __str__(self):
        return "Товар: " + str(self.product) + ", " + "Заказ: " + str(self.order.code)

    class Meta:
        verbose_name_plural = 'Товары в заказах'

