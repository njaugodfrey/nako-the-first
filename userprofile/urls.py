from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'userprofile'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'userprofile/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^account/basic/$', views.UserUpdateView.as_view(), name='user-profile-basic'),
    url(r'^account/extra/$', views.ProfileUpdateView.as_view(), name='user-profile-extra'),
    url(r'^u/(?P<slug>[-\w\d]+)/$', views.ProfileDetailView.as_view(), name='user-profile'),
]
