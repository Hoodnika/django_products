from django.db import models

from products.special_elements import NULLABLE
from users.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='дата последнего изменения', auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(TimeStampMixin):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(**NULLABLE, upload_to='products/photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField()
    view_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    published = models.BooleanField(verbose_name='Опубликован', default=False)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('can_edit_published', 'Может менять опубликованность продукта'),
            ('can_edit_description', 'Может редактировать описание продукта'),
            ('can_edit_category', 'Может редактировать категорию продукта')
        ]
