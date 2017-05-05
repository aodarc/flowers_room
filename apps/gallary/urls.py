from django.conf.urls import url
from django.views.generic import TemplateView

from apps.gallary.views import GalleryView, PhotoView

urlpatterns = [
    url(r'/(?P<pk>\d+)/photos$', PhotoView.as_view(), name='gallery-photo'),
    url(r'/(?P<pk>\d+)/photos/(?P<p_pk>\d+)$', PhotoView.as_view(), name='gallery-photo-detail'),
    url(r'$', GalleryView.as_view(), name='gallery'),
]
