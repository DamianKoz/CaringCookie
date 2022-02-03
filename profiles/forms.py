
from opcode import haslocal
from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class NewProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(required=False)
    city = forms.CharField(required=False)
    university = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ("avatar", "bio", "city", "university")

    def save(self, commit=True):
        profile = super(NewProfileForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    city = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    university = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'city', 'university']


