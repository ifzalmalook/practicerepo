from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Project, Category
from .forms import ProjectForm
from django.utils.text import slugify
from django.urls import path, reverse_lazy


# Create your views here.

# def LikeView(request, slug):
#     post = get_object_or_404(Project, slug=slug)
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('full_project', args=[slug]))


def home(request):
    return render(request, 'home.html')


class Projects(ListView):
    """
    List of Projects
    """
    template_name = 'projects/projects.html'
    model = Project

        

    def get_queryset(self, **kwargs):
        search = self.request.GET.get("query")
        if search:
            projects = self.model.objects.filter(
                Q(title__icontains=search)|
                Q(description__icontains=search)|
                Q(category__name__icontains=search) #search relating to a foreign key

            )

            return projects
        
        else:

            return self.model.objects.all()
            

        

        
    




class AddProject(LoginRequiredMixin, CreateView):
    """
    View for adding craft projects
    """
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.author = self.request.user

        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, "Your project has been added!")
        return super(AddProject, self).form_valid(form)


#view to generate full project page from the link on project listings
@login_required
def full_project(request, slug):
    # Retrieve the project object using the provided slug
    queryset = Project.objects.filter(slug=slug)
    project = get_object_or_404(queryset, slug=slug)
    msg = False

    if request.user.is_authenticated:
        user=request.user

        if project.likes.filter(id=user.id).exists():
            msg = True

    
   
    if request.method == 'POST':

        if request.user.is_authenticated:
            user=request.user

        if project.likes.filter(id=user.id).exists():
            project.likes.remove(user)
            msg=False
        
        else:
            project.likes.add(user)
            msg=True
    
    
    # Pass the project object to the template context
    return render(
        request,
        "projects/full_project.html",
        {"project": project,
        "msg":msg
        }  # Use the correct variable name here
    )

#View to delete project

class DeleteProject(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects')

    def test_func(self):
        return self.request.user == self.get_object().author

    #add success message
    def form_valid(self, form):
        # If the form is valid, display a success message
        messages.success(self.request, 'The project has been removed!')
        return super().form_valid(form)

class EditProject(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'projects/edit_project.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')

    def test_func(self):
        return self.request.user == self.get_object().author

    #add success message
    def form_valid(self, form):
        # If the form is valid, display a success message
        messages.success(self.request, 'Your project has been updated!')
        return super().form_valid(form)