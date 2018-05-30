from django.contrib import admin

# Register your models here.
from apps.problems.models import Question, Illness, QuestionToIllness


class IllnessInline(admin.StackedInline):
    model = QuestionToIllness


class QuestionAdmin(admin.ModelAdmin):
    fields = ('title', )
    inlines = (IllnessInline, )


class IllnessAdmin(admin.ModelAdmin):
    fields = ('name', 'flowers', 'solution')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Illness, IllnessAdmin)
