from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('',views.ListView.as_view(), name='list'),
    # path('signup/', views.signup, name='signup'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('profile/create/',views.ProfileCreate.as_view(),name="profile_create"),
    
]