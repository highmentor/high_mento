from django.shortcuts import render
from django.views.generic import CreateView, ListView
from . import forms
from django.urls import reverse_lazy
from .models import User
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    
class AccountsList(ListView):
    model = User
    template_name = 'accounts/accounts_list.html'