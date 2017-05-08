from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from apps.userprofile.forms import RegistrationForm, LogInForm


class RegistrationView(View):
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                login(request, user)

        return redirect(request.META['HTTP_REFERER'])


class LogInView(View):
    def post(self, request):
        form = LogInForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)

        return redirect(request.META['HTTP_REFERER'])


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_page')
