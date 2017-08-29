from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import ComicSeries, ComicIssue

# Create your views here.


class ComicsHome(generic.ListView):
    context_object_name = 'all_series'
    template_name = "comics/comics_home.html"

    def get_queryset(self):
        return ComicSeries.objects.all()


class ComicsDetailView(generic.DetailView):
    model = ComicSeries
    context_object_name = 'series'
    template_name = "comics/series_detail.html"


class ComicSeriesCreate(CreateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']


class ComicSeriesUpdate(UpdateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']


class ComicSeriesDelete(DeleteView):
    model = ComicSeries
    success_url = reverse_lazy('comics:comics_home')


# Series Issues

class IssueList(generic.ListView):
    context_object_name = 'all_issues'
    template_name = "comics/series_detail.html"

    def get_queryset(self):
        return ComicIssue.objects.all()

class IssueDetailView(generic.DetailView):
    model = ComicIssue
    context_object_name = 'comic'
    template_name = "comics/issue.html"


class ComicIssueCreate(CreateView):
    model = ComicIssue
    fields = ['title', 'cover', 'description', 'artist']


class ComicIssueUpdate(UpdateView):
    model = ComicIssue
    fields = ['title', 'cover', 'description', 'artist']


class ComicIssueDelete(DeleteView):
    model = ComicSeries
    success_url = reverse_lazy('comics:series_detail')


