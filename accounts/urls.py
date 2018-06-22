"""MealPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from .views import ProfilePageDetail, CreateUserView, LogoutView, LoginView, UpdateUserView, UpdatePasswordView

app_name = 'accounts'
urlpatterns = [
    path('', ProfilePageDetail.as_view(), name='profile'),
    path('signup', CreateUserView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='signin'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('update', UpdateUserView.as_view(), name='update'),
    path('update/password', UpdatePasswordView.as_view(), name='update.password')
]
