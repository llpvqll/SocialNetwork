from django.shortcuts import render


def index(request):
    template_name = 'base/base.html'
    context = {}
    return render(request, template_name, context)


