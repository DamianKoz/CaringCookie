from cProfile import label
from django import forms
from django.http import request

TYPES = (
        ('Suche', 'Suche'),
        ('Biete', 'Biete')
    )
class CreateBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
    type= forms.ChoiceField(label="Typ",choices=TYPES)
    
class ChangeBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
