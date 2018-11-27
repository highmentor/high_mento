from django.shortcuts import render
from .models import University, University_review
from django.db import models
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ReviewForm
from django.db.models import Avg

# Create your views here.

class UniversityList(ListView):
    model = University
    
class University_detail(DetailView):
    model = University
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating_avg'] = self.get_object().university_review_set.aggregate(Avg('rating'))['rating__avg']
        return context
        
    
class University_create(CreateView):
    model = University_review
    form_class = ReviewForm
    # fields = ['university','major']
    
    def form_valid(self, form):
        form.instance.university_id = self.kwargs.get('university_id')
        return super().form_valid(form)