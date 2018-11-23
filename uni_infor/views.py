from django.shortcuts import render
from .models import University, University_review
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class UniversityList(ListView):
    model = University
    
class University_detail(DetailView):
    model = University
    
class University_create(CreateView):
    model = University_review
    field = ['university','major']