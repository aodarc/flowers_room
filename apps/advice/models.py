from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Advice(models.Model):
    created = models.DateField(auto_now_add=True, verbose_name='Доданий')
    image = models.ImageField(upload_to='posts')
    author = models.ForeignKey(to=User, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextUploadingField(verbose_name="Опис")

    def __str__(self):
        return 'ID({}) {}'.format(self.id, self.title)

    def save(self, *args, **kwargs):
        self.description = str(self.description).replace('&nbsp;', ' ')
        super().save(*args, **kwargs)


class Answer(models.Model):
    advice = models.ForeignKey(to=Advice, related_name='advices')
    text = RichTextUploadingField(verbose_name="Текст коментаря")
    expert = models.ForeignKey(to=User,
                               null=True,
                               verbose_name='Автор',
                               related_name='experts',
                               on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID({}) PostID({}) Expert({})'.format(self.id, self.advice_id, self.expert)

    def save(self, *args, **kwargs):
        self.text = str(self.text).replace('&nbsp;', ' ')
        super().save(*args, **kwargs)
