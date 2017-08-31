from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from comics.models import ComicIssue, ComicSeries
from .forms import UserForm

# Create your views here.

def home(request):
    series =  ComicSeries.objects.order_by('-date_uploaded').all()[:5]
    return render(request, 'home/home.html', {'series':series})


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # clean (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')
            
            return render(request, self.template_name, {'form': form})
