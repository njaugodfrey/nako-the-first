from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from comics.models import ComicIssue, ComicSeries
from .models import Profile
from .forms import SignUpForm, UserProfileForm
from .tokens import account_activation_token

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('userprofile/account_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your Nako account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete registration')
    else:
        form = SignUpForm()
    return render(request, 'userprofile/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home:home')
    else:
        return HttpResponse('Activation link is invalid.')


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
    
