from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class UserProfileForm(forms.ModelForm):
    header = forms.ImageField(required = False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required = False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    website = forms.CharField(required = False, widget=forms.URLInput(attrs={'class': 'form-control', 'maxlength': '200', 'placeholder': 'https://www...'}))
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '30', 'placeholder': 'Gatundu, Kiambu, Kenya.'}))
    date_birth = forms.CharField(required = False, widget=forms.DateInput(attrs={'class': 'form-control', 'maxlength': '10', 'placeholder': 'YYYY-MM-DD'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'maxlength': '200', 'rows': 3, 'placeholder': 'Hi! Im a comic artist/fan...'}))    

    class Meta:
        model = Profile
        fields = ('avatar', 'website', 'location', 'date_birth', 'bio')
