from . import views
from django.urls import path


app_name = 'questions'

urlpatterns = [
    path('', views.List.as_view(), name ='list'),
    path('new/', views.Create.as_view(), name='reate'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    path('<int:pk>/edit/', views.Update.as_view(), name='edit'),
    
    path('<int:question_id>/answer_create/', views.Answer_Create.as_view(), name='answer_create'),
    path('<int:question_id>/answer_delete/', views.Answer_Delete.as_view(), name='answer_delete'), 
    path('<int:question_id>/answer_update/', views.Answer_Update.as_view(), name='answer_update'), 
    

]
