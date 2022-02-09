from cProfile import label
from django import forms
from blog.models import Category
from django.http import request

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
    category = forms.ModelChoiceField(label="Kategorie", queryset=Category.objects.all())
    
class ChangeBlogForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    content = forms.CharField(label='Beschreibung', widget=forms.Textarea)
    type= forms.ChoiceField(label="Typ",choices=TYPES)
    producttype = forms.ChoiceField(label="ProduktTyp", choices=PRODUCTTYPES)
    category = forms.ModelChoiceField(label="Kategorie", queryset=Category.objects.all())
