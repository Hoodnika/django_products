# Generated by Django 5.0.3 on 2024-05-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version_app', '0002_alter_version_version_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_num',
            field=models.FloatField(verbose_name='Номер версии'),
        ),
    ]
