from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_menu, name="menu"),
    path('HTL', views.sort, name="sorted"),
    path('LTH', views.sort, name="sorted"),
]