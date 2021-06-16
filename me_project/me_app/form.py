from .models import Idea, Comment 

class CommentForm(form.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)