from django.views.generic.base import ContextMixin

from apps.forum.models import Post, Category, Comment
from apps.gallary.models import Photo


class RightSideContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'right_posts': Post.objects.all()[:3],
            'right_categories': Category.objects.all(),
            'right_comments': Comment.objects.all()[:5]
        })

        return context


class FooterContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'footer_photos': Photo.objects.all()[:12],
            'footer_posts': Post.objects.all()[:6],
        })

        return context
