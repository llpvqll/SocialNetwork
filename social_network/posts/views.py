from django.shortcuts import render
from .models import Post
from .post_form import PostForm
# Create your views here.


def main(request):
    template_name = 'posts.html'
    context = {}
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        form_for_posts = PostForm
        posts = Post.objects.all()
        context['posts'] = posts
        context['form'] = form_for_posts
        if form.is_valid():
            data = form.cleadend_data
            form.save()
        return render(request, template_name, context)

    else:
        return render(request, template_name, context)
