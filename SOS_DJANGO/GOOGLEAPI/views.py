from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import logout_then_login
from ORS import template


def logout_view(request):
    print("LLLLLLLLLLLL")
    logout_then_login(request)
    return  render (request, 'Login.html')
