from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва', db_index=True, unique=True)
    image = models.ImageField(upload_to='albums/', verbose_name='Головне зображення')
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description = str(self.description).replace('&nbsp;', ' ')
        super().save(*args, **kwargs)


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    owner = models.ForeignKey(to=User, related_name='photos', verbose_name='Завантажено')
    description = RichTextUploadingField(verbose_name="Опис")
    album = models.ForeignKey(Album, related_name='photos')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    image = models.ImageField(upload_to='photos/', verbose_name='Картинка')

    def save(self, *args, **kwargs):
        self.description = str(self.description).replace('&nbsp;', ' ')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
