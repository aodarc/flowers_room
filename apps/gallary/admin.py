from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget

# Register your models here.
from apps.gallary.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }


class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)