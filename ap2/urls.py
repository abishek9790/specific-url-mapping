from django.urls import path
from ap2.views import *
app_name='bb'
urlpatterns=[
    path('seco/',seco,name='seco'),
]