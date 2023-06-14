# app1/urls.py

from django.urls import path, re_path

from . import views
from .views import contact, about, programs, login_view, logout_user, register, stripePay, home, program_details

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^.*programs/$', programs, name='programs'),
    re_path(r'^.*about/$', about, name='about'),
    re_path(r'^.*contact/$', contact, name='contact'),
    re_path(r'^.*login/$', login_view, name='login'),
    re_path(r'^.*logout_user/$', logout_user, name='logout'),
    re_path(r'^.*register/$', register, name='register'),
    re_path(r'^.*donate/$', stripePay, name='donate'),
    re_path(r'^.*programs/(?P<program_id>\d+)/$', program_details, name='program_details'),
    path('charts/', views.chart_view, name='chart_view'),

]
