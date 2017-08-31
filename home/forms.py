from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for User form."""

        model = User
        fields = ('username', 'email', 'password',)

