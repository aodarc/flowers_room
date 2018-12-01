from django.conf.urls import url

from apps.advice.views import AdviceView, SingleAdvice, add_advice

app_name = 'advice'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', SingleAdvice.as_view(), name='detail'),
    url(r'^add_advice$', add_advice, name='add_advice'),
    url(r'^$', AdviceView.as_view(), name='list'),
]
