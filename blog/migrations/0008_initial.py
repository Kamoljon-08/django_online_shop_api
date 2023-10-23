# Generated by Django 4.2.3 on 2023-10-23 11:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
        ('blog', '0007_remove_blogimagemodel_blog_remove_blogmodel_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('block', models.BooleanField(default=False)),
                ('description', ckeditor.fields.RichTextField(max_length=100000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('block', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to='blog/')),
                ('sequence_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('block', models.BooleanField(default=False)),
                ('message', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]
