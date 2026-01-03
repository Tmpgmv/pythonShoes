from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    patronymic = models.CharField(300)

    def get_full_name(self):
        return super().first_name + " " + self.patronymic + " " + super().last_name