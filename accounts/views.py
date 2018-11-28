from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import User
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

class AccountsList(ListView):
    model = User
    template_name = 'accounts/accounts_list.html'
    
def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
        if signup_form.is_valid():
            # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
            signup_form.signup()
            return redirect('accounts:login')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)