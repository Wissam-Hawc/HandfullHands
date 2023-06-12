# app1/urls.py

from django.urls import path
from .views import contact, about, programs, login_view, logout_user, register, stripePay, home, program_details

urlpatterns = [
    path('', home, name='home'),
    path('programs/', programs, name='programs'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('donate/', stripePay, name='donate'),
    path('programs/<int:program_id>/',program_details, name='program_details'),
    path('register/', register, name='register'),

]
