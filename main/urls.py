from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.frontPage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login , name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
