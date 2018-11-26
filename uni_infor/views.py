from django.shortcuts import render, redirect, resolve_url
from .models import University, University_review
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .forms import PostForm

# Create your views here.

class UniversityList(ListView):
    model = University
    
class University_detail(DetailView):
    model = University
    
class University_create(CreateView):
    model = University_review
    fields = ['major']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['university'] = University.objects.get(pk=self.kwargs.get('university_id'))
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['university'] = University.objects.get(pk=self.kwargs.get('university_id'))
        return context
        
    def form_valid(self, form):
        form.instance.university = University.objects.get(pk=self.kwargs.get('university_id'))
        return super().form_valid(form)
            
