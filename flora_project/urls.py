"""flora_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from apps.userprofile.views import RegistrationView, LogInView, LogOutView
from flora_project.views import MainPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', MainPageView.as_view(), name='main_page'),
    url(r'^forum/', include('apps.forum.urls')),
    url(r'^gallery/', include('apps.gallary.urls')),
    url(r'^questions/', include('apps.problems.urls')),
    url(r'^log-in$', LogInView.as_view(), name='login'),
    url(r'^log-out$', LogOutView.as_view(), name='logout'),
    url(r'^registration$', RegistrationView.as_view(), name='registration')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
