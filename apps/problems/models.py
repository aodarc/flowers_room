from django.db import models

# Create your models here.
from apps.flowers.models import Flowers


class Illness(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Назва хвороби'
    )

    flowers = models.ManyToManyField(
        to=Flowers,
        related_name='illnesses'
    )
    solution = models.TextField(
        verbose_name='Підходи до вирішення'
    )


class Question(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Питання'
    )
    illnesses = models.ManyToManyField(
        to=Illness,
        through='QuestionToIllness',
        related_name='questions'
    )

    def __str__(self):
        return self.title


class QuestionToIllness(models.Model):
    illness = models.ForeignKey(
        to=Illness
    )
    question = models.ForeignKey(
        to=Question
    )
    weight = models.IntegerField(
        verbose_name='Вага відповідності'
    )
