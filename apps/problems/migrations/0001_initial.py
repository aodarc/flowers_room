# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-27 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва хвороби')),
                ('solution', models.TextField(verbose_name='Підходи до вирішення')),
                ('flowers', models.ManyToManyField(related_name='illnesses', to='flowers.Flowers')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Питання')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionToIllness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(verbose_name='Вага відповідності')),
                ('illness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Illness')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='illnesses',
            field=models.ManyToManyField(related_name='questions', through='problems.QuestionToIllness', to='problems.Illness'),
        ),
    ]
