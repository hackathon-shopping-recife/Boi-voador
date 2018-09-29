from django.urls import path

from .controllers.client import *

urlpatterns = [
    path('auth/', Client.as_view(), name='view_client'),
]