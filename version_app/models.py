from django.db import models

from products.models import TimeStampMixin
from products.special_elements import NULLABLE


class Version(TimeStampMixin):
    version_num = models.FloatField(verbose_name='Номер версии')
    version_name = models.CharField(verbose_name='Название версии', max_length=100, **NULLABLE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    is_active = models.BooleanField(default=True, verbose_name='Активность версии')

    def __str__(self):
        return f'{self.product} - {self.version_num}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
