from ckeditor.widgets import CKEditorWidget
from django import forms

from apps.forum.models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='comment'))

    class Meta:
        model = Comment
        fields = ('text',)
