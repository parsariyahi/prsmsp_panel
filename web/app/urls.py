from django.urls import path

from app.views import *

urlpatterns = [
    path('', index),
    path('add/panel', add_panel),
]