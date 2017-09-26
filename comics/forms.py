from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a comment?', 'maxlength': '500', 'rows': '6'}))

    class Meta:

        model = Comment
        fields = ('text',)

