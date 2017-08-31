from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.UserRegFormView.as_view(), name='register')
]
