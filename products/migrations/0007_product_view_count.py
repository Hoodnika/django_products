# Generated by Django 5.0.3 on 2024-05-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
