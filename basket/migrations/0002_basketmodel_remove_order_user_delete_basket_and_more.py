# Generated by Django 4.2.3 on 2023-09-30 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productmodel_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.SmallIntegerField(default=0)),
                ('total_count', models.SmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcolormodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel')),
                ('sizes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsizemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
