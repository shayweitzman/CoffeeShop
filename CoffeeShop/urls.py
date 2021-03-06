"""CoffeeShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from Home import views as HomeViews
from Authentication import views as AuthViews
from Cart import views as CartViews
from Tables import views as TablesViews
from orders import views as OrdersViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeViews.home, name="homepage"),
    path('AddClient/', AuthViews.AddClient, name="AddClient"),
    path('AddBarista/', AuthViews.AddBarista, name="AddBarista"),
    path('Login/', AuthViews.loginU, name="Login"),
    path('logout/', AuthViews.logoutuser, name="logoutuser"),
    path('Cart/', CartViews.Cart, name="cart"),
    path('PlaceOrder/', OrdersViews.PlaceOrder, name="PlaceOrder"),
    path('myOrders/', OrdersViews.myOrders, name="myOrders"),
    path('', HomeViews.home, name="homepage"),
    re_path('menuShow', include('Menu.urls')),
    path('makeOrder/', include('Tables.urls')),
    path('makeOrder/', TablesViews.order, name="order"),
    path('editTableOrder/', include('orders.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
