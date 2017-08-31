from django import forms
from django.contrib.auth.models import User

class UserRegForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    class Meta:
        """Meta definition for User form."""

        model = User
        fields = ('username', 'email', 'password',)

class UserLoginForm(forms.ModelForm):
    """Form definition for UserLogin."""
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    class Meta:
        """Meta definition for UserLoginform."""

        model = User
        fields = ('email', 'password',)

