from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from apps.advice.forms import AnswerForm, AdviceForm
from apps.advice.models import Advice
from flora_project.mixins import FooterContextMixin, RightSideContextMixin


class AdviceView(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'advice/advices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Advice.objects.filter(author=self.request.user)
        context['form'] = AdviceForm()

        return context


class SingleAdvice(FooterContextMixin, RightSideContextMixin, TemplateView):
    template_name = 'advice/advice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post'] = get_object_or_404(klass=Advice, id=self.kwargs['pk'])
        context['form'] = AnswerForm()

        return context


def add_advice(request):

    form = AdviceForm(request.POST, files=request.FILES)

    if form.is_valid():
        data = form.cleaned_data.copy()
        data['author'] = request.user
        Advice.objects.create(
            **data
        )

    return redirect(reverse('advice:list'))
