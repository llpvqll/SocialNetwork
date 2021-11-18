from django.forms import ModelForm
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'email', 'password')





