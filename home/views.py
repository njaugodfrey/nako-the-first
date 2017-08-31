from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from comics.models import ComicIssue, ComicSeries
from .forms import SignUpForm

# Create your views here.

def home(request):
    series =  ComicSeries.objects.order_by('-date_uploaded').all()[:5]
    return render(request, 'home/home.html', {'series':series})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})