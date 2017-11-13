from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^blog/$', views.PostListView.as_view(), name='blog_home'),
    url(r'^blog/new$', views.PostCreate.as_view(), name='blog-create'),
    url(r'^blog/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='blog-detail'),
    url(r'^blog/search/$', views.SearchListView.as_view(), name='blog-search-results'),
]
