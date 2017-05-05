from django.conf.urls import url
from django.views.generic import TemplateView

from apps.gallary.views import GalleryView

urlpatterns = [
    url(r'$', GalleryView.as_view(), name='gallery')
]