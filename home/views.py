from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'
from django.contrib.auth import logout