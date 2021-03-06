"""donation_boi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from donation_boi.views import *


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='stores', permanent=True), name="home"),
    path('stores/<int:pk>', StoreDetailView.as_view(), name="store_detail"),
    path('stores', StoreList.as_view(), name="stores"),
    path('items/<int:pk>', ItemDetailView.as_view(), name="item_detail"),
    path('login', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout', auth_views.auth_logout, name="logout"),
    path('register', register, name="register"),
    path('search', search, name="search")
]
