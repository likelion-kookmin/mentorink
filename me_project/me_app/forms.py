from django import forms
from .models import Idea, Comment 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'author',
            'message'
        )