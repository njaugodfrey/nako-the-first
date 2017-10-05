from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from comics.models import ComicIssue, ComicSeries
from .models import Profile
from .forms import SignUpForm, UserProfileForm

# Create your views here.

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
    return render(request, 'userprofile/signup.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = SignUpForm
    template_name = "userprofile/userprofile_edit_userinfo.html"
    
    def get_success_url(self, *args, **kwargs):
        profile = self.get_object()
        return reverse('userprofile:user-profile', kwargs={'slug':profile.username})

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = "userprofile/userprofile_edit_userprofile.html"
    success_url = ('home:home')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        profile = self.get_object()
        return reverse('userprofile:user-profile', kwargs={'slug':profile.user.username})

    def get_object(self):
        return self.request.user.profile


class ProfileDetailView(generic.DetailView):
    model = User
    template_name = "userprofile/userprofile.html"
    slug_field = 'username'
    context_object_name = 'usr'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['series'] = ComicSeries.objects.filter(user = self.get_object())
        return context
    
