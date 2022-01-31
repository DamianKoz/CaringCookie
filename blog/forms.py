from django import forms
from django.http import request

class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
    
class ChangeBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
