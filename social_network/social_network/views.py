from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from profiles.forms import ProfileForm


def index(request):
    template_name = 'base/base.html'
    context = {}
    return render(request, template_name, context)


class RegisterFormView(FormView):
    form_class = ProfileForm
    success_url = '/login/'
    template_name = 'register.html'

    def form_valid(self, form):
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
