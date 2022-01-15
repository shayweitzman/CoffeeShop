from django.urls import path, re_path
from . import views
import re

urlpatterns = [
    path('/', views.all_menu, name="menu"),
    re_path(r'[/?][a-zA-Z]+', views.sort, name="sorted"),
    #path('HTL', views.sort, name="sorted"),
    #path('LTH', views.sort, name="sorted"),
]