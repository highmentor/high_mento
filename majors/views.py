from django.shortcuts import render, reverse
from .models import Major, Major_review
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class MajorList(LoginRequiredMixin,ListView):
    model = Major
    template_name = 'majors/major_list.html'
    

class MajorCreate(LoginRequiredMixin, CreateView):
    model = Major
    fields = ('major_id','major_intro')
    template_name = 'majors/major_form.html'
    
class MajorDetailView(DetailView):
    model = Major
    
class MajorReviewList(ListView):
    model = Major_review
    
class MajorReviewCreate(CreateView):
    model = Major_review
    fields = ('content',)
    template_name = 'majors/major_review_form.html'
    
    def form_valid(self, form):
        form.instance.major_id = self.kwargs.get('major_id')
        return super().form_valid(form)