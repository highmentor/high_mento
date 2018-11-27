from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView
from .forms import UserForm
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

class AccountsList(ListView):
    model = User
    template_name = 'accounts/accounts_list.html'
    
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
        return render(request, 'accounts/signup.html', {'form': form})