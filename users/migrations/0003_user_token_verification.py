# Generated by Django 5.0.3 on 2024-05-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token_verification',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='код верификации'),
        ),
    ]
