from django.shortcuts import render

from comics.models import ComicSeries
from userprofile.models import Profile

# Create your views here.

def home(request):
    home_series =  ComicSeries.objects.order_by('-date_uploaded').all()[:5]
    return render(request, 'home/home.html', {'home_series':home_series})

def about(request):
    return render(request, 'about/about.html', {})
