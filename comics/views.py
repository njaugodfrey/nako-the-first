from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ComicSeriesCreate(LoginRequiredMixin, CreateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ComicSeriesCreate, self).form_valid(form)


class ComicSeriesUpdate(LoginRequiredMixin, UpdateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']


class ComicSeriesDelete(LoginRequiredMixin, DeleteView):
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


class ComicIssueCreate(LoginRequiredMixin, CreateView):
    model = ComicIssue
    fields = ['title', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ComicIssueCreate, self).form_valid(form)


class ComicIssueUpdate(LoginRequiredMixin, UpdateView):
    model = ComicIssue
    fields = ['issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']


class ComicIssueDelete(LoginRequiredMixin, DeleteView):
    model = ComicIssue
    success_url = reverse_lazy('comics:comics_home')


