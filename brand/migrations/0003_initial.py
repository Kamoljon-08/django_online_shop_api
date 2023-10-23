# Generated by Django 4.2.3 on 2023-10-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0002_delete_brandmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('block', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='brand/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
