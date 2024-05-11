from django.db import models

NULLABLE = {'blank': True, 'null': True}


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

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


# class Blog(TimeStampMixin):
#     title = models.CharField(max_length=150, verbose_name='Заголовок')
#     slug = models.CharField(max_length=150, verbose_name='Ссылка', unique=True)
#     content = models.TextField(verbose_name='Содержание')
#     image = models.ImageField(**NULLABLE, upload_to='blogs/photo')
#     published = models.BooleanField(verbose_name='Опубликовано', default=False)
#     view_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = 'блог'
#         verbose_name_plural = 'блоги'