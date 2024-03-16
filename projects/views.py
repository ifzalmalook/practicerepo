from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.utils.text import slugify

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
    success_url = '/projects/'

    def form_valid(self, form):
        form.instance.author = self.request.user

        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, "Your project has been added!")
        return super(AddProject, self).form_valid(form)


#view to generate full project page from the link on project listings
def full_project(request, slug):
    # Retrieve the project object using the provided slug
    queryset = Project.objects.filter(slug=slug)
    project = get_object_or_404(queryset, slug=slug)
    
    # Pass the project object to the template context
    return render(
        request,
        "projects/full_project.html",
        {"project": project}  # Use the correct variable name here
    )
