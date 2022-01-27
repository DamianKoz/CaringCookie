from django import forms

class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
    

