from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import logout
from projects.models import Project

# Create your views here.

class Home(ListView):
    template_name = 'home/home.html'
    model = Project

    def get_queryset(self):
        return self.model.objects.all()[:3]
# from django.contrib.auth import logout