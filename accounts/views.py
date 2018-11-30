from django.shortcuts import render,redirect,resolve_url
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import User, Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AccountsList(ListView):
    model = User
    template_name = 'accounts/accounts_list.html'

class SignUp(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('accounts:profile_create')   
    
    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class ProfileCreate(LoginRequiredMixin,CreateView):
    model = Profile
    fields = ['major',]
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return super().form_valid(form)
