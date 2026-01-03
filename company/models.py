from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контрагенты'