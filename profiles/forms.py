
from opcode import haslocal
from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    vorname = forms.CharField(required=True)
    nachname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("vorname", "nachname", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.vorname = self.cleaned_data['vorname']
        user.nachname = self.cleaned_data['nachname']
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)
    city = forms.CharField(label='Stadt', max_length=30, required=False)
    university = forms.CharField(label='Uni', max_length=30, required=False)
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'city', 'university']


