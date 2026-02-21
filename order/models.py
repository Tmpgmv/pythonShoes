from django.db import models
from django.db.models import Max
from django.forms.widgets import DateInput
from django.utils import timezone


class Order(models.Model):
    # SELECT setval('order_order_id_seq', (SELECT MAX(id) FROM order_order));
    STATUSES = [("Новый", "Новый"), ("Завершен", "Завершен")]

    order_date = models.DateField(auto_created=True,
                                  default=timezone.now,
                                  verbose_name="Дата заказа")
    delivery_date = models.DateField(verbose_name="Дата доставки")
    office = models.ForeignKey('office.Office',
                               on_delete=models.CASCADE,
                               verbose_name="Пункт выдачи:")
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE,
                             verbose_name="Клиент")
    code = models.IntegerField(unique=True,
                               blank=True,
                               verbose_name="Код получения")
    status = models.CharField(max_length=10,
                              choices=STATUSES,
                              default='Новый',
                              verbose_name="Статус")

    def save(self, *args, **kwargs):
        if self.pk is None:  # New instance
            max_code = Order.objects.aggregate(Max('code'))['code__max']
            self.code = (max_code or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Заказы'
