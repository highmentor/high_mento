from django.shortcuts import render
from .models import Major, Major_review
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.

class MajorList(ListView):
    model = Major
    template_name = 'majors/major_list.html'
