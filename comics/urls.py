from django.conf.urls import url
from . import views

app_name = 'comics'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^comics/$', views.ComicsHome.as_view(), name='comics_home'),
    url(r'^comics/z(?P<pk>[0-9]+)/$',views.ComicsDetailView.as_view(), name='series_detail'),
    url(r'^comicseries/add/$', views.ComicSeriesCreate.as_view(), name='comic-series-add'),
    url(r'^comicseries/(?P<pk>[0-9]+)/$', views.ComicSeriesUpdate.as_view(), name='comic-series-update'),
    url(r'^comicseries/(?P<pk>[0-9]+)/delete/$', views.ComicSeriesDelete.as_view(), name='comic-series-delete'),
    url(r'^comicissue/(?P<pk>[0-9]+)/$',views.IssueDetailView.as_view(), name='issue_detail'),
]

