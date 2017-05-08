from django.views.generic import TemplateView

from apps.forum.models import Post
from apps.gallary.models import Album, Photo
from flora_project.mixins import FooterContextMixin


class MainPageView(FooterContextMixin, TemplateView):
    template_name = 'main_page/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photoalbums'] = Album.objects.all()
        context['random_photos'] = Photo.objects.all().order_by('?')[:12]
        context['lasted_post'] = Post.objects.all()[:3]

        return context