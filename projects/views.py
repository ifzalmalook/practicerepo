from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


class Projects(ListView):
    """
    List of Projects
    """
    template_name = 'projects/projects.html'
    model = Project
    




class AddProject(LoginRequiredMixin, CreateView):
    """
    View for adding craft projects
    """
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm
    succes_url = '/projects/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your project has been added!")
        return super(AddProject, self).form_valid(form)