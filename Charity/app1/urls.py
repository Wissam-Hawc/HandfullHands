# app1/urls.py

from django.urls import path
from . import views
from .views import contact, about, programs, login_view, logout_user, details

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', programs, name='programs'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('details/', details, name='details'),
]
