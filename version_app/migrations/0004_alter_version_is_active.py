# Generated by Django 5.0.3 on 2024-05-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version_app', '0003_alter_version_version_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность версии'),
        ),
    ]
