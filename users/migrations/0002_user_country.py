# Generated by Django 5.0.3 on 2024-05-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='страна'),
        ),
    ]
