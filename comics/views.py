from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComicSeries, ComicIssue, Comment
from .forms import CommentForm

# Create your views here.


class ComicsHome(generic.ListView):
    context_object_name = 'all_series'
    template_name = "comics/comics_home.html"
    paginate_by = 5

    def get_queryset(self):
        return ComicSeries.objects.order_by('-date_uploaded').all()


class ComicsDetailView(generic.DetailView):
    model = ComicSeries
    slug_field = 'comicseries_id'
    context_object_name = 'series'
    template_name = "comics/series_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ComicsDetailView, self).get_context_data(**kwargs)
        context['issues'] = ComicIssue.objects.filter(title=self.object.id).select_related().order_by('-date_added')
        return context


class ComicSeriesCreate(LoginRequiredMixin, CreateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ComicSeriesCreate, self).form_valid(form)


class ComicSeriesUpdate(LoginRequiredMixin, UpdateView):
    model = ComicSeries
    fields = ['title', 'cover', 'description', 'artist']

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('comics:comics_home')
        return super(ComicSeriesUpdate, self).dispatch(request, *args, **kwargs)


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
    fields = ['issue', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.title = ComicSeries.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()
        return redirect('comics:series_detail', pk=obj.title.id, slug=obj.title.slug)


class ComicIssueUpdate(LoginRequiredMixin, UpdateView):
    model = ComicIssue
    fields = ['issue', 'issue_title', 'issue_cover', 'issue_description', 'issue_cover', 'issue_file']

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('comics:comics_home')
        return super(ComicIssueUpdate, self).dispatch(request, *args, **kwargs)


class ComicIssueDelete(LoginRequiredMixin, DeleteView):
    model = ComicIssue
    
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('comics:comics_home')
        return super(ComicIssueDelete, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        comicissue = self.get_object()
        return reverse_lazy('comics:series_detail', 
            kwargs={'id':comicissue.title.id, 'slug':comicissue.title.slug}
        )
    

# comments

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
        return redirect('comics:issue_detail', 
            pk=obj.issue.id, issue_slug=obj.issue.issue_slug, slug=obj.issue.title.slug
        )
