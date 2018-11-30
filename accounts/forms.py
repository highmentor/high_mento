from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class UserCreateForm(UserCreationForm):
    
    class Meta:
        # fields = '__all__'
        fields = ('username','email','password1','password2')
        model = get_user_model()
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'