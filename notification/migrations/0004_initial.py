# Generated by Django 4.2.3 on 2023-10-23 11:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
        ('notification', '0003_delete_notificationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', ckeditor.fields.RichTextField(max_length=500)),
                ('block', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]
