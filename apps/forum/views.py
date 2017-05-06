from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from apps.forum.models import Post, Comment
from flora_project.mixins import FooterContextMixin, RightSideContextMixin
from .forms import CommentForm


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
        context['form'] = CommentForm()

        return context


def add_comment(request, pk):

    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                author=request.user,
                post=post,
                text=form.cleaned_data['text']
            )

    return redirect(reverse('forum_single', kwargs={'pk': pk}))
