from django import forms
from django.forms.models import inlineformset_factory
from .models import Comment, IssuePanel, ComicIssue

class ComicIssueForm(forms.ModelForm):

    class Meta:

        model = ComicIssue
        fields = ('issue', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file')


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a comment?', 'maxlength': '500', 'rows': '6'}))

    class Meta:

        model = Comment
        fields = ('text',)
    
class IssuePanelForm(forms.ModelForm):

    class Meta:

        model = IssuePanel
        fields = ('panel',)


IssuePanelFormSet = inlineformset_factory(ComicIssue, IssuePanel, form=IssuePanelForm, extra=3)
