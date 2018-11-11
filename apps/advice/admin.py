from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models


# Register your models here.
from apps.advice.models import Advice, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class AdviceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    inlines = [
        AnswerInline
    ]


admin.site.register(Advice, AdviceAdmin)
admin.site.register(Answer)
