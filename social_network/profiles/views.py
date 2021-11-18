from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def profile_view(request):
    template_name = 'profile.html'
    context = {}
    if request.user.is_authenticated:
        profile = request.user
        # username = Profile.username
        # context['username'] = username
        context['profile'] = profile
        return render(request, template_name, context)
    else:
        return render(request, template_name, context)





