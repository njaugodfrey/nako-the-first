from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import operator
from django.db.models import Q

from .models import Post

# Create your views here.


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'text', 'image',]

    def form_valid(self, form):
        user = self.request.user
        if user.is_staff:
            form.instance.author = self.request.user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('home:home')


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'all_posts'
    paginate_by = 10
    queryset = Post.objects.order_by('-date_posted').all()
    template_name = "blog/blog_home.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'


class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'text', 'image',]

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.author == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('blog:blog_home')
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)


class PostDelete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_home')

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.author == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('blog:blog_home')
        return super(PostDelete, self).dispatch(request, *args, **kwargs)



class SearchListView(PostListView):
    paginate_by = 10
    
    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset_list = query.split()
            result = result.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ).distinct()
        return result

