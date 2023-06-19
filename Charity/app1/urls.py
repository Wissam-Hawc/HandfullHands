from .views import home, programs, about, contact, login_view, logout_user, register, stripePay, program_details, \
    whyHopfullhand
from django.urls import path, re_path


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
    re_path(r'^.*hopfullhand/$', whyHopfullhand, name='why_hopfullhand'),
    # path('chatbot/', chatbot, name='chatbot'),

]

