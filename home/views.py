from django.shortcuts import render

from comics.models import ComicSeries

# Create your views here.

def home(request):
    home_series =  ComicSeries.objects.order_by('-date_uploaded').all()[:6]
    return render(request, 'home/home.html', {'home_series':home_series})
