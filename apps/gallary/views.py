from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from apps.gallary.models import Album, Photo


class GalleryView(TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Album.objects.all()[:12]

        context['data'] = queryset
        context['albums'] = True

        return context


class PhotoView(TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Photo.objects.filter(album_id=self.kwargs['pk'])[:12]

        context['data'] = queryset
        context['photos'] = True

        return context

class PhotoDetailView(TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Photo.objects.get(id=self.kwargs['pk'])

        context['photo'] = queryset

        return context
