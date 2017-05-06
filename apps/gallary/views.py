from django.views.generic import TemplateView

from apps.gallary.models import Album, Photo
from flora_project.mixins import RightSideContextMixin, FooterContextMixin


class GalleryView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Album.objects.all()[:12]

        context['data'] = queryset
        context['albums'] = True

        return context


class PhotoView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'galary/gallery.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Photo.objects.filter(album_id=self.kwargs['pk'])[:12]

        context['album_id'] = self.kwargs['pk']
        context['data'] = queryset
        context['photos'] = True

        return context


class PhotoDetailView(FooterContextMixin, TemplateView):
    template_name = 'galary/photo_detail.html'

    def get_context_data(self, **kwargs):
        context = {}
        queryset = Photo.objects.get(id=self.kwargs['p_pk'])

        context['photo'] = queryset

        return context
