from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView,logout_then_login
from GOOGLEAPI import views

urlpatterns = [
    path('logout/',  views.logout_view),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="index1.html"),name="login"),
    
    # path('logout', LogoutView.as_view()),

]
