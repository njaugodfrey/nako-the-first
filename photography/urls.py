from django.conf.urls import url
from . import views

app_name = 'photography'

urlpatterns = [
    url(r'^photographs/$', views.PhotosList.as_view(), name='photos_home'),
    url(r'^photographs/(?P<pk>[0-9]+)/$',views.PhotosDetail.as_view(), name='photos_detail'),
    url(r'^photographs/add/$',views.PhotographyCreate.as_view(), name='photos-add'),
    url(r'^photographs/(?P<pk>[0-9]+)/$',views.PhotographyUpdateView.as_view(), name='photos-update'),
    url(r'^photographs/(?P<pk>[0-9]+)/delete/$',views.PhotographyDeleteView.as_view(), name='photos-delete'),
]

