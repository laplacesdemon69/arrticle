from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content']
