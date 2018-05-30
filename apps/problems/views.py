from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from apps.problems.models import Question
from apps.problems.serializers import QuestionSerializer
from flora_project.paginators import OneResultPerPagePaginator


class QuestionPageView(TemplateView):
    template_name = 'problems/question_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # by first question
        context['question'] = Question.objects.first()
        context['next_question'] = reverse('questions-list') + '?page=2'
        return context


class QuestionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = QuestionSerializer
    pagination_class = OneResultPerPagePaginator

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer_class()(question)
        return Response(serializer.data)
