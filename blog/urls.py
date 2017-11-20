from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^blog/$', views.PostListView.as_view(), name='blog_home'),
    url(r'^blog/post/new/$', views.PostCreate.as_view(), name='post-create'),
    url(r'^blog/post/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^blog/post/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/update/$', 
            views.PostUpdate.as_view(), name='post-update'
        ),
    url(r'^blog/post/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/delete/$', 
            views.PostDelete.as_view(), name='post-delete'
        ),
    url(r'^blog/search/$', views.SearchListView.as_view(), name='blog-search-results'),
]
