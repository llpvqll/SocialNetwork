from django.db import models
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email

    def dict(self):
        obj = {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
        }
        return obj

