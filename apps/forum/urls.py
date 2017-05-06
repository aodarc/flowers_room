from django.conf.urls import url

from apps.forum.views import ForumView, SinglePost

urlpatterns = [
    url(r'^(?P<pk>\d+)$', SinglePost.as_view(), name='forum_single'),
    url(r'^$', ForumView.as_view(), name='forum'),
]
