from django import forms
from inbox.models import MessageModel

class ThreadForm(forms.Form):
  username = forms.CharField(label='', max_length=100)
  #username = forms.ModelChoiceField(label="Gib einen Nutzernamen an, um mit dem Chatten anzufangen.", queryset=User.objects.all())

class MessageForm(forms.ModelForm):
  #message = forms.CharField(label='', max_length=1000)
  body = forms.CharField(label='', max_length=1000)
  image = forms.ImageField(label='Send an Image', required=False)
  class Meta:
    model = MessageModel
    fields = ['body', 'image']