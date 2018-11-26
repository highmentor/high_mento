from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "majors"

urlpatterns = [
    path('', views.MajorList.as_view(), name = 'list'),
    path('create/', views.MajorCreate.as_view(), name='create'),
    path('<int:pk>/',views.MajorDetailView.as_view(),name='detail'),
    
]