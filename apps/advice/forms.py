from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.advice.models import Advice, Answer


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='answer'))

    class Meta:
        model = Answer
        fields = ('text',)


class AdviceForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    image = forms.ImageField()
    description = forms.CharField(widget=CKEditorWidget(config_name='advice'))

    class Meta:
        model = Advice
        fields = ('title', 'image', 'description')
