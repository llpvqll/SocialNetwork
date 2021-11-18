from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator
from profiles.models import Profile


class Post(models.Model):

    post_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/img',
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
                              blank=True)
    post_author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    post_text = models.TextField(max_length=1000)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_name}-{self.post_author}-{self.liked}'


LIKE_CHOICE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICE, max_length=8)
    updates = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.post}-{self.value}'
