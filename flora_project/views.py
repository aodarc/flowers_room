from django.views.generic import TemplateView

from apps.forum.models import Post
from apps.gallary.models import Album, Photo
from flora_project.mixins import FooterContextMixin, RightSideContextMixin


class MainPageView(FooterContextMixin, TemplateView):
    template_name = 'main_page/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photoalbums'] = Album.objects.all()
        context['random_photos'] = Photo.objects.all().order_by('?')[:12]
        context['lasted_post'] = Post.objects.all()[:3]
        context['comments_block'] = Post.objects.filter(
            comments__isnull=False).prefetch_related('comments').distinct()[:5]

        return context


class HelpPageView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'help_page/main.html'


class ResultHelpPageView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'help_page/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(id__in=[8,9])

        return context
