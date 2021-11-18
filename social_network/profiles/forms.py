from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




