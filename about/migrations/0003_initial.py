# Generated by Django 4.2.3 on 2023-10-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0002_delete_companyfilemodel_delete_companymembermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='about/')),
                ('title', models.CharField(max_length=20)),
                ('block', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyMemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('job', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('block', models.BooleanField(blank=True, default=True)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
