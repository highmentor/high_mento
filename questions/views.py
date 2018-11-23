from django.shortcuts import render
from django.views.generic import (View,TemplateView, DetailView,CreateView,ListView, UpdateView, DeleteView)
##새로추가
from django.http import HttpResponse ## 새로추가

from .models import Question, Answer
from django.urls import reverse_lazy

from .forms import AnswerForm

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
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm()
        return context
    
class Answer_Create(CreateView):
    model = Answer
    fields=('title','content')
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.question_id = self.kwargs.get('question_id')
        # self.object.question = Question.objects.get(pk=self.kwargs.get('question_id'))
        self.object.save()
        
        return super().form_valid(form)
        
class Answer_Update(UpdateView):
    model = Answer
    fields=('title','content',)

class Answer_Delete(DeleteView):
    model = Answer
    success_url = reverse_lazy('question:list')