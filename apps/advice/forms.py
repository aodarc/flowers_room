from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.advice.models import Advice, Answer


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='answer'))

    class Meta:
        model = Answer
        fields = ('text',)


class AdviceForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    image = forms.ImageField(label='Зображення')
    description = forms.CharField(widget=CKEditorWidget(config_name='advice'), label='Опис')

    class Meta:
        model = Advice
        fields = ('title', 'image', 'description')
