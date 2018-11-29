from django.shortcuts import render
from .models import Major, Major_review
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.

class MajorList(ListView):
    model = Major
    template_name = 'majors/major_list.html'
    

class MajorCreate(CreateView):
    model = Major
    fields = ('major_id','major_intro')
    template_name = 'majors/majors_form.html'
    
class MajorDetailView(DetailView):
    model = Major