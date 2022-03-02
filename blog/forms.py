from cProfile import label
from django import forms
from blog.models import Category
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
    category = forms.ModelChoiceField(label="Kategorie", queryset=Category.objects.all())


    class Meta:
        model = Blog
        fields = ['title', 'content', 'type', 'producttype']

class CreateBlogFormExtended(CreateBlogForm):
    images = forms.FileField(label="Bilder" ,required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(CreateBlogForm.Meta):
        fields = CreateBlogForm.Meta.fields + ['images']

class SendMailForm(forms.Form):
    sending_mail = forms.CharField(label='Ihre Mail-Adresse', max_length=150)
    subject = forms.CharField(label='Betreff', max_length=100 )
    message = forms.CharField(label='Ihre Nachricht', widget=forms.Textarea)
    

        