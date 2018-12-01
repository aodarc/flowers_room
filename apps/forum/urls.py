from django.conf.urls import url

from apps.forum.views import ForumView, SinglePost, TopicView, add_comment, SingleTopicPost

urlpatterns = [
    url(r'^(?P<pk>\d+)/add_comment$', add_comment, name='forum-add-comment'),
    url(r'^(?P<pk>\d+)$', SinglePost.as_view(), name='forum_single'),
    url(r'^topic/(?P<pk>\d+)$', SingleTopicPost.as_view(), name='topic_single'),
    url(r'^topic/$', TopicView.as_view(), name='topic'),
    url(r'^$', ForumView.as_view(), name='forum'),
]
