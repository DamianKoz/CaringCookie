from cProfile import label
from django import forms
from django.http import request

from blog.models import Blog

TYPES = (
        ('Suche', 'Suche'),
        ('Biete', 'Biete')
    )
PRODUCTTYPES = (
        ('Produkt', 'Produkt'),
        ('Dienstleistung', 'Dienstleistung')
    )

class CreateBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
    type= forms.ChoiceField(label="Typ",choices=TYPES)
    producttype = forms.ChoiceField(label="ProduktTyp", choices=PRODUCTTYPES)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'type']

class CreateBlogFormExtended(CreateBlogForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(CreateBlogForm.Meta):
        fields = CreateBlogForm.Meta.fields + ['images',]
    
class ChangeBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
    type= forms.ChoiceField(label="Typ",choices=TYPES)
    producttype = forms.ChoiceField(label="ProduktTyp", choices=PRODUCTTYPES)

