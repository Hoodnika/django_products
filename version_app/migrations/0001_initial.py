# Generated by Django 5.0.3 on 2024-05-09 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='дата последнего изменения')),
                ('version_num', models.FloatField(verbose_name='Версия')),
                ('version_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='verbose_name=Название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
