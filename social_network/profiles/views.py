from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Profile
# Create your views here.


class List(TemplateView):
    template_name = 'profile.html'

    def profile_view(self, request):
        context = {}
        if request.user.is_authenticated:
            profile = Profile.objects.all()
            context['profile'] = profile
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)





