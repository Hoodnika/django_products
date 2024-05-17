from django.contrib.auth.models import AbstractUser
from django.db import models

from products.special_elements import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    token_verification = models.CharField(max_length=50, verbose_name='код верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

