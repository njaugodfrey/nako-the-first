from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComicSeries, ComicIssue, Comment
from .forms import CommentForm

# Create your views here.


class ComicsHome(generic.ListView):
    context_object_name = 'all_series'
    template_name = "comics/comics_home.html"

    def get_queryset(self):
        return ComicSeries.objects.order_by('-date_uploaded').all()


class ComicsDetailView(generic.DetailView):
    model = ComicSeries
    slug_field = 'comicseries_id'
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
    
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('comics:comics_home')
        return super(ComicSeriesDelete, self).dispatch(request, *args, **kwargs)


# Series Issues

class IssueDetailView(generic.DetailView):
    model = ComicIssue
    slug_field = 'comicissue_id'
    context_object_name = 'comic'
    template_name = "comics/issue.html"
    
    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(issue=self.object.id).select_related()
        return context
    

class ComicIssueCreate(LoginRequiredMixin, CreateView):
    model = ComicIssue
    slug_field = 'comicseries_id'
    fields = ['issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.title = ComicSeries.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()
        return redirect('series_detail', pk=obj.title.id)


class ComicIssueUpdate(LoginRequiredMixin, UpdateView):
    model = ComicIssue
    fields = ['issue', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']


class ComicIssueDelete(LoginRequiredMixin, DeleteView):
    model = ComicIssue
    success_url = reverse_lazy('comics:comics_home')
    
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('comics:comics_home')
        return super(ComicIssueDelete, self).dispatch(request, *args, **kwargs)
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    slug_field = 'comicissue_id'
    form_class = CommentForm
    template_name = "comics/comment_new.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.issue = ComicIssue.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()
        return redirect('issue_detail', pk=obj.issue.id)