from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d-%m-%Y')}"
