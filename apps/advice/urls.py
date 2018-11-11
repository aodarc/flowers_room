from django.conf.urls import url

from apps.advice.views import AdviceView, SingleAdvice

app_name = 'advice'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', SingleAdvice.as_view(), name='detail'),
    url(r'^$', AdviceView.as_view(), name='list'),
]
