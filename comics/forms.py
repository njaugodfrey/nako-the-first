from django import forms
from multiupload.fields import MultiFileField
from .models import Comment, IssuePanel, ComicIssue

class PanelsForm(forms.ModelForm):

    class Meta:

        model = ComicIssue
        fields = ('issue', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file')
    
    panels = MultiFileField(min_num=1, max_num=20, max_file_size=2048*2048*5)

    def save(self, commit=True):
        instance = super(PanelsForm, self).save()
        for each in self.cleaned_data['panels']:
            IssuePanel.objects.create(panel=each, issue=instance)
        return instance


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a comment?', 'maxlength': '500', 'rows': '6'}))

    class Meta:

        model = Comment
        fields = ('text',)
    
