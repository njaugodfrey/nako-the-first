from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Photos

# Create your views here.


class PhotosList(generic.ListView):
    context_object_name = 'pics'
    template_name = "photography/photos_home.html"

    def get_queryset(self):
        return Photos.objects.all()


class PhotosDetail(generic.DetailView):
    model = Photos
    template_name = "photography/photos_detail.html"


class PhotographyCreate(CreateView):
    model = Photos
    fields = ['image', 'caption', 'photographer', 'studio']


class PhotographyUpdateView(UpdateView):
    model = Photos
    fields = ['image', 'caption', 'photographer', 'studio']


class PhotographyDeleteView(DeleteView):
    model = Photos
    success_url = reverse_lazy('photography:photos_home')


