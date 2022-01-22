from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TableOrders, name="table_orders"),
    path('<int:table_id>/', views.editTorder, name="edit_torder"),
]