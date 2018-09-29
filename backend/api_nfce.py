from django.urls import path

from .controllers.nfce import *

urlpatterns = [
    path('data/', Nfce.as_view(), name='view_client'),
]