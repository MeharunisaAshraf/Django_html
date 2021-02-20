"""Onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from .views import Index, Signup, Login, Logout, Cart, CheckOut, Cover, OrderView, Staff
from .middlewares.auth import simple_middleware
urlpatterns = [
    path('', Cover.as_view(), name='CoverPage'),
    path('home', Index.as_view(), name='HomePage'),
    path('signup', Signup.as_view(), name='SignupPage'),
    path('login', Login.as_view(), name='LoginPage'),
    path('logout', Logout.as_view()),
    path('cart', simple_middleware(Cart.as_view()), name='cart'),
    path('checkout',CheckOut.as_view(), name='CheckoutPage'),
    path('staff', Staff.as_view(), name='StaffPage'),
    path('orders', OrderView.as_view(), name='OrderPage'),
]
