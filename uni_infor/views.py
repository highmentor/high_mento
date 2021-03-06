from django.shortcuts import render
from .models import University, University_review
#University_major_data
from django.db import models
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ReviewForm
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UniversityList(ListView):
    model = University
    
class University_detail(DetailView):
    model = University
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if ((self.get_object().university_review_set.aggregate(Avg('rating1'))['rating1__avg'] == None) &
            (self.get_object().university_review_set.aggregate(Avg('rating1'))['rating1__avg'] == None) &
            (self.get_object().university_review_set.aggregate(Avg('rating1'))['rating1__avg'] == None)):
            context['rating1_avg'] = 0
            context['rating2_avg'] = 0
            context['rating3_avg'] = 0
            context['rating_total_avg'] = 0
            return context
        
        else:
            context['rating1_avg'] = round(self.get_object().university_review_set.aggregate(Avg('rating1'))['rating1__avg'],1)
            context['rating2_avg'] = round(self.get_object().university_review_set.aggregate(Avg('rating2'))['rating2__avg'],1)
            context['rating3_avg'] = round(self.get_object().university_review_set.aggregate(Avg('rating3'))['rating3__avg'],1)
            context['rating_total_avg'] = round((context['rating1_avg'] + context['rating2_avg'] + context['rating3_avg']) / 3.0,1)
            return context
        
    
class University_create(LoginRequiredMixin,CreateView):
    model = University_review
    form_class = ReviewForm
    # fields = ['major','content']
    
    def get_form_kwargs(self):
        print(self.request)
        kwargs = super().get_form_kwargs()
        kwargs.update({'university_id': self.kwargs.get('university_id')})
        return kwargs
    
    def get_context_data(self, **kwargs):
        print(self.request)
        context = super().get_context_data(**kwargs)
        context['university'] = University.objects.get(pk=self.kwargs.get('university_id'))
        return context
    
    def form_valid(self, form):
        
        print(self.request)
        form.instance.university_id = self.kwargs.get('university_id')
        return super().form_valid(form)