from django import forms
from .models import University, University_review

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea(attrs = {'class':'editable'}))