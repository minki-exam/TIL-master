from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from faker import Faker
f= Faker()


class User(AbstractUser):
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')


    def __str__(self):
        return self.username

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            u = cls()
            u.username = f.first_name()
            u.set_password('123456')
            u.save()
       