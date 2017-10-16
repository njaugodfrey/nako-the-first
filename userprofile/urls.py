from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'userprofile'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'userprofile/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, 
        {'template_name': 'userprofile/password_reset_form.html'}, name='password_reset'
        ),
    url(r'^password_reset/done/$', auth_views.password_reset_done, 
        {'template_name': 'userprofile/password_reset_done.html'}, name='password_reset_done'
        ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        auth_views.password_reset_confirm, {'template_name': 'userprofile/password_reset_confirm.html'}, 
        name='password_reset_confirm'
        ),
    url(r'^reset/done/$', auth_views.password_reset_complete, 
        {'template_name': 'userprofile/password_reset_complete.html'}, name='password_reset_complete'
        ),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'
        ),
    url(r'^account/basic/$', views.UserUpdateView.as_view(), name='user-profile-basic'),
    url(r'^account/extra/$', views.ProfileUpdateView.as_view(), name='user-profile-extra'),
    url(r'^u/(?P<slug>[-\w\d]+)/$', views.ProfileDetailView.as_view(), name='user-profile'),
]
