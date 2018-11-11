# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-11 21:17
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Доданий')),
                ('image', models.ImageField(upload_to='posts')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Опис')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст коментаря')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('advice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advices', to='advice.Advice')),
                ('expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
