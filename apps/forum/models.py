from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категорія')
    description = models.TextField(max_length=1000, verbose_name='Короткий опис')

    def __str__(self):
        return 'ID({}) {}'.format(self.id, self.name)


class Post(models.Model):
    created = models.DateField(auto_now_add=True, verbose_name='Доданий')
    author = models.ForeignKey(to=User, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextUploadingField(verbose_name="Опис")
    category = models.ForeignKey(to=Category, related_name='posts')

    def __str__(self):
        return 'ID({}) {}'.format(self.id, self.title)


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тег', db_index=True)
    posts = models.ManyToManyField(to=Post, related_name='tags')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments')
    text = RichTextUploadingField(verbose_name="Текст коментаря")
    author = models.ForeignKey(to=User, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID({}) PostID({}) Author({})'.format(self.id, self.post_id, self.author_id)


class Answer(Comment):
    comment = models.ForeignKey(to=Comment, verbose_name='До коментаря', related_name='answers')
