from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from apps.forum.models import Post
from flora_project.mixins import FooterContextMixin, RightSideContextMixin


class ForumView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'forum/forum.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.all()

        return context


class SinglePost(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'forum/forum_single_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post'] = get_object_or_404(klass=Post, id=self.kwargs['pk'])

        return context
