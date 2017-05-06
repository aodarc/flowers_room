from django.conf.urls import url

from apps.gallary.views import GalleryView, PhotoView, PhotoDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/photos$', PhotoView.as_view(), name='gallery-photo'),
    url(r'^(?P<pk>\d+)/photos/(?P<p_pk>\d+)$', PhotoDetailView.as_view(), name='gallery-photo-detail'),
    url(r'^$', GalleryView.as_view(), name='gallery'),
]
