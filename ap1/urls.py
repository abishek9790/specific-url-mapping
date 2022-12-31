from django.urls import path
from ap1.views import *
app_name='aa'
urlpatterns=[
    path('fir/',fir,name='fir'),
]