from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.problems.views import QuestionPageView, QuestionsViewSet

router = DefaultRouter()
router.register(r'', QuestionsViewSet, base_name='questions')

urlpatterns = [
    # url(r'^(?P<pk>\d+)/photos$', PhotoView.as_view(), name='gallery-photo'),
    url(r'^help/$', QuestionPageView.as_view(), name='question-page'),
]

urlpatterns += router.urls
