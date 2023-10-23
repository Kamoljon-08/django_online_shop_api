# Generated by Django 4.2.2 on 2023-08-21 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productcolormodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]