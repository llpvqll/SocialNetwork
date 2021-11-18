from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['post_name', 'image', 'post_text']