from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    patronymic = models.CharField(max_length=300,
                                  verbose_name="Отчество")

    def get_full_name(self):
        return super().first_name + " " + self.patronymic + " " + super().last_name

    def is_admin(self):
        return self.groups.filter(name='Администратор').exists()

    def is_manager(self):
        return self.groups.filter(name='Менеджер').exists()

    def is_client(self):
        return self.groups.filter(name='Авторизированный клиент').exists()

    def __str__(self):
        return self.get_full_name()


    def role(self):
        if self.is_admin():
            return 'Администратор'
        elif self.is_client():
            return 'Авторизированный клиент'
        elif self.is_manager():
            return 'Менеджер'
        else:
            return 'Гость'