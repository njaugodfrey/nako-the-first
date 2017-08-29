from django.conf.urls import url
from . import views

app_name = 'comics'

urlpatterns = [
    url(r'^comics/$', views.ComicsHome.as_view(), name='comics_home'),
    url(r'^comics/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/$',views.ComicsDetailView.as_view(), name='series_detail'),
    url(r'^comic/series/add/$', views.ComicSeriesCreate.as_view(), name='comic-series-add'),
    url(r'^comic/series/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/$', 
            views.ComicSeriesUpdate.as_view(), name='comic-series-update'
        ),
    url(r'^comic/series/(?P<slug>[-\w\d]+)-(?P<pk>[0-9]+)/delete/$', 
            views.ComicSeriesDelete.as_view(), name='comic-series-delete'
        ),
    url(r'^comics/issue/(?P<issue_slug>[-\w\d]+)-(?P<pk>[0-9]+)/$',
            views.IssueDetailView.as_view(), name='issue_detail'
        ),
    url(r'^comic/issue/add/$', views.ComicIssueCreate.as_view(), name='comic-issue-add'),
    url(r'^comic/issue/(?P<issue_slug>[-\w\d]+)-(?P<pk>[0-9]+)/$', 
            views.ComicIssueUpdate.as_view(), name='comic-Issue-update'
        ),
    url(r'^comic/issue/(?P<issue_slug>[-\w\d]+)-(?P<pk>[0-9]+)/delete/$', 
            views.ComicIssueDelete.as_view(), name='comic-issue-delete'
        ),
]

