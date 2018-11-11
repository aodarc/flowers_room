from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.advice.models import Advice


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='comment'))

    class Meta:
        model = Advice
        fields = ('text',)
