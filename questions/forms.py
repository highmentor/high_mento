from django import forms

from .models import Answer

class AnswerForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()
    
    class Meta:
        model = Answer
        fields = ('title','content',)
    