
from django.urls import path, include, re_path
from . import views
import datetime




urlpatterns = [
    path('', views.order, name="order"),
]