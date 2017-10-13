from django.shortcuts import render
from django.views import generic
import operator
from django.db.models import Q

from comics.models import ComicSeries
from comics.views import ComicsHome
from userprofile.models import Profile

# Create your views here.

def home(request):
    home_series =  ComicSeries.objects.order_by('-date_uploaded').all()[:5]
    return render(request, 'home/home.html', {'home_series':home_series})

def about(request):
    return render(request, 'about/about.html', {})


class SearchListView(ComicsHome):
    paginate_by = 10

    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset_list = query.split()
            result = result.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
        return result

