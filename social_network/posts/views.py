from django.shortcuts import render

# Create your views here.


def main(request):
    template_name = 'posts.html'
    context = {}
    return render(request, template_name, context)
