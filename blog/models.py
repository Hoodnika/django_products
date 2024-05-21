from django.db import models

from products.models import TimeStampMixin
from products.special_elements import NULLABLE
from users.models import User


class Blog(TimeStampMixin):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='Ссылка', unique=True)
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(**NULLABLE, upload_to='blogs/photo')
    published = models.BooleanField(verbose_name='Опубликовано', default=False)
    view_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец статьи', **NULLABLE)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        permissions = [
            ('can_edit_published', 'Может менять опубликованность блога'),
        ]


class Comment(TimeStampMixin):
    description = models.TextField(verbose_name='Комментарий')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='статья')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'