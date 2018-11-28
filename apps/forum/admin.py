from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models


# Register your models here.
from apps.forum.models import Post, Comment, Tag, Answer, Category, Topic


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

#
# class AlbumAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': CKEditorWidget()},
#     }

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Answer)
