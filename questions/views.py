from django.shortcuts import render
from django.views.generic import (View,TemplateView, DetailView,CreateView,ListView, UpdateView, DeleteView)
##새로추가
from django.http import HttpResponse ## 새로추가

from .models import Question
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    
    return render(request,'questions/base.html')
    
class Create(CreateView):
    model = Question
    fields=('title','high_major','content')
    
class List(ListView):
    model = Question
    template_name = 'questions/question_list.html'
    
class Delete(DeleteView):
    model = Question
    success_url = reverse_lazy('questions:list')
    
class Update(UpdateView):
    model = Question
    fields=('title','high_major','content',)
    
class Detail(DetailView):
    model = Question
    template_name = 'questions/question_detail.html'