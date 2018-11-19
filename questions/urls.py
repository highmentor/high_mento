from . import views
from django.urls import path


app_name = 'questions'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.Create.as_view(), name='create'),
    path('list/', views.List.as_view(), name ='list'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('update/<int:pk>', views.Update.as_view()),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    
    # path('cbv/',views.CBView.as_view()),
    # path('cbv_index/',views.IndexView.as_view()),
    # path('<int:pk>/',views.SchoolDetailView.as_view()), #url 요청이 들어오면 스쿨디테일뷰시작

]
