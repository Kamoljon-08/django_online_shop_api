# Generated by Django 4.2.3 on 2023-10-20 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_remove_notificationmodel_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NotificationModel',
        ),
    ]
