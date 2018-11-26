from django.urls import path
from . import views

app_name = 'universities'

urlpatterns = [
    path('',views.UniversityList.as_view(),name='list'),
    path('<int:pk>/',views.University_detail.as_view(),name='detail'),
    path('<int:university_id>/new/',views.University_create.as_view(), name = 'create'),
    # university_id라고 해야 review id랑헷갈리지 않기 때문이다.
    ]