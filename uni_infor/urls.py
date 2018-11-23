from django.urls import path
from . import views

app_name = 'universities'

urlpatterns = [
    path('',views.UniversityList.as_view(),name='list'),
    path('<int:pk>/',views.University_detail.as_view(),name='detail'),
    path('<int:pk>/new/',views.University_create.as_view(), name = 'create'),
    ]