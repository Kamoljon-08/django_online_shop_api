# Generated by Django 4.2.2 on 2023-08-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productcolormodel_productsizemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolormodel',
            name='color',
            field=models.TextField(max_length=20),
        ),
    ]
