from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from apps.gallary.models import Album


class GalleryView(TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Album.objects.all()[:12]

        context['data'] = queryset
        context['albums'] = True

        return context
